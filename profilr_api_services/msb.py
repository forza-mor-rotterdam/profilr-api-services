import copy

from .default_incident_api import DefaultIncidentAPIService
from .exceptions import ApiServiceNotFoundException
from .conf import conf
from requests import Response
from typing import TypedDict, List, cast, Union

DEFAULT_FILTERS = {
    "wijken": [],
    "buurten": [],
    "afdelingen": [],
    "groepen": [],
    "onderwerpItems": [],
}
DEFAULT_PROFILE = {"filters": DEFAULT_FILTERS}
VALID_FILTERS = ("buurten", "afdelingen", "onderwerpItems")

class UnValidatedFiltersType(TypedDict, totals=False):
    pass

class ValidatedFiltersType(TypedDict):
    afdelingen: List[str]
    buurten: List[str]
    onderwerpItems: List[str]

class MsbResultType(TypedDict, totals=False):
    pass

class MsbResponseType(TypedDict, totals=False):
    success: TypedDict
    result: Union[List[MsbResultType], str]

class MSBService(DefaultIncidentAPIService):

    def validate_filters(self, filters: UnValidatedFiltersType) -> ValidatedFiltersType:
        valid_filters: ValidatedFiltersType = copy.deepcopy(cast(ValidatedFiltersType, filters))
        {
            k: v if type(v) == list else [v] if type(v) in [str, int, float] else []
            for k, v in valid_filters.items()
            if k in VALID_FILTERS
        }
        for k in VALID_FILTERS:
            if not valid_filters.get(k):
                valid_filters[k] = []
        return valid_filters

    def process_response(self, response: Response) -> Union[List[MsbResultType], str]:
        response_dict: MsbResponseType = response.json()
        return response_dict.get("result")

    def logout(self) -> MsbResultType:
        return self.do_request("logout", no_cache=True)

    def login(self, username: str, password: str):
        data = {
            "uid": username,
            "pwd": password,
        }
        response_data = self.do_request(
            "login",
            user_token=None,
            method=MSBService.POST,
            data=data,
            no_cache=True,
            raw_response=True,
        )
        response_data = response_data.json()
        return bool(response_data.get("success")), response_data.get("result")

    def get_user_info(self, user_token):
        response = self.do_request("gebruikerinfo", user_token, no_cache=True, raw_response=True)
        return response.json()

    def get_list(self, user_token, data={}, no_cache=False):
        return self.do_request(
            "msb/openmeldingen", user_token, MSBService.POST, data, no_cache
        )

    def get_detail(self, melding_id, user_token):
        result = self.do_request(
            f"msb/melding/{melding_id}", user_token, cache_timeout=0
        )
        if result.get("id") is None:
            raise ApiServiceNotFoundException(f"Melding not found: {melding_id}")
        return result

    def get_mutatieregels(self, melding_id, user_token):
        return self.do_request(
            f"msb/melding/{melding_id}/mutatieregels", user_token, cache_timeout=30
        )

    def get_foto(self, foto_id, user_token, thumbnail=False):
        data = {}
        if thumbnail:
            data.update({"thumbnail": thumbnail})
        return self.do_request(
            f"msb/melding/foto/{foto_id}",
            user_token,
            data=data,
            raw_response=True,
            cache_timeout=60 * 60,
        )

    def get_wijken(self, user_token):
        return self.do_request("wijken", user_token, cache_timeout=60 * 60 * 24)

    def get_onderwerpgroepen(self, user_token):
        return self.do_request(
            "msb/onderwerpgroepen", user_token, cache_timeout=60 * 60 * 24
        )

    def get_afdelingen(self, user_token):
        return self.do_request("msb/afdelingen", user_token, cache_timeout=60 * 60 * 24)

    def get_afdeling_relaties(self, user_token, afdeling_id):
        if not conf.MSB_ENABLE_AFDELING_RELATIES_ENDPOINT:
            return {"success": True, "result": {}}
        return self.do_request(
            f"msb/afdeling/{afdeling_id}", user_token, cache_timeout=60 * 60 * 24
        )

    def melding_aanmaken(self, user_token: str, data: dict):
        """
        {
            fotos: [{
                dataUrl: "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABkA...,
                isEindsituatie: false,
            }]
            huisnummer: "114",
            melderInformeren: false,
            meldingtype: "S",
            omschrijving: "Er ligt hier vuil op straat",
            onderwerp: "47",
            spoed: false,
            straat: "66400",
            x: 89789,
            y: 438634
        }
        """
        if conf.MSB_API_URL.startswith(conf.MSB_API_URL_PRODUCTION):
            return {
                "success": True,
                "result": "Melding ******* is aangemaakt.",
                "messages": [
                    "Melding ******* ingevoerd",
                    "Foto bij melding ******* is opgeslagen.",
                    "Mail voor afdeling bij nieuwe melding opgeslagen",
                    "De afdeling van melding ******* is aangepast.",
                    "Mail voor afdeling bij doorverwijzen opgeslagen",
                    "Melding ******* is aangemaakt.",
                ],
                "warnings": [],
                "errors": [],
            }
        return self.do_request(
            "msb/melding",
            user_token,
            data=data,
            method=MSBService.POST,
            no_cache=True,
            raw_response=True,
        )

    def afhandelen(self, melding_id: str, user_token: str, data: dict):
        """
        {
            "meldingId":2407629,
            "behandelaar":"Behandelaar naam",
            "meldingType":"O",
            "afhandelOpmerking":"De gemeente is aan de slag gegaan met uw melding en volgens onze gegevens is het probleem opgelost. Daarom sluiten we uw melding.",
            "straat":"55832",
            "huisnummer":"205",
            "plaatsbepaling":null,
            "x":92396,
            "y":437830
        }

        {
            "meldingId":2407694,
            "behandelaar":"Behandelaar naam",
            "meldingType":"N",
            "redenAfhandelenNiet":"73",
            "afhandelOpmerking":"De (brom)fiets is volgens onze richtlijnen geen wrak. Daarom verwijderen we deze niet. Kijk op https://www.rotterdam.nl/wonen-leven/handhaving/ voor meer informatie. We sluiten uw melding.",
            "straat":"82821",
            "huisnummer":"54",
            "plaatsbepaling":"Alternatieve plaatsbepaling",
            "x":92355,
            "y":437451,
            "fotos":[{}]
        }
        """
        if conf.MSB_ENABLE_MELDING_AFHANDELEN:
            response = self.do_request(
                f"msb/melding/{melding_id}/afhandelen",
                user_token,
                data=data,
                method=MSBService.POST,
                no_cache=True,
                raw_response=True,
            )
            return response.json()
        return self.get_detail(melding_id, user_token)


# incident = MSBService(f"{conf.MSB_API_URL}/sbmob/api")
