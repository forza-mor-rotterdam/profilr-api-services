from .base import APIService

""" 
    In the comments the fields that are used. 
    Fields that do exist in the database but not used yet are left out.
"""
class DefaultIncidentAPIService(APIService):
    def validate_filters(self):
        raise NotImplementedError("You must implement validate_filters")

    def logout(self):
        raise NotImplementedError("You must implement logout")

    def login(self):
        raise NotImplementedError("You must implement login")

    def get_user_info(self):
        raise NotImplementedError("You must implement get_user_info")

    """ list
        "spoed": Boolean,
        "datumMelding": "YYYY-MM-DDTHH:MM:SS",
        "afdeling": {
            "id": String,
            "omschrijving": String,
        },
        "id": Number,
        "status": String,
        "onderwerp": {
            "id": String,
            "omschrijving": String
        },
        "omschrijving": String,
        "locatie": {
            "adres": {
                "straatNummer": String,
                "straatNaam": String,
                "huisnummer": String,
            },
            "x": Number,
            "y": Number,
        },
    """
    def get_list(self):
        raise NotImplementedError("You must implement get_list")

    """ detail
        "success": Boolean,
        "result": {
            "id": Number,
            "status": String,
            "meldingType": String,
            "datumMelding": "YYYY-MM-DDTHH:MM:SS",
            "onderwerp": {
                "id": String,
                "omschrijving": String
            },
            "afdeling": {
                "id": String,
                "omschrijving": String,
            },
            "omschrijving": String,
            "behandelaar": String,
            "melder": {
                "herkomst": String,
                "naam": String,
                "telefoon": String,
                "informeren": String["Ja", "Nee"],
            },
            "locatie": {
                "buurtNummer": String,
                "subbuurt": String,
                "adres": {
                    "straatNummer": String,
                    "straatNaam": String,
                    "huisnummer": String,
                },
                "plaatsbepaling": String,
                "x": Number,
                "y": Number,
            },
            "fotos": [],
            "magDoorverwijzen": Boolean,
            "magAfhandelen": Boolean,
        }
    """
    def get_detail(self):
        raise NotImplementedError("You must implement get_detail")

    """ mutatieregels
        "success": Boolean,
        "result": [
            {
                "datum": String,
                "gebruiker": String,
                "opmerking": String,
                "details": [
                    {
                        "key": String,
                        "value": String
                    }
                ],
            }
        ]
    """
    def get_mutatieregels(self):
        raise NotImplementedError("You must implement get_mutatieregels")

    def get_foto(self):
        raise NotImplementedError("You must implement get_foto")

    """ wijken
        "success": Boolean,
        "result": [
            {
                "code": String,
                "omschrijving": String,
                "buurten": [
                    {   
                        "code": String,
                        "omschrijving": String
                    }
                ],
            }
        ],
    """
    def get_wijken(self):
        raise NotImplementedError("You must implement get_foto")

    """ onderwerpgroepen
        "success": Boolean,
        "result": [
            {
                "code": String,
                "omschrijving": String,
                "onderwerpen": [
                    {
                        "code": String,
                        "omschrijving": String,
                        "magDoorverwijzen": Boolean,
                    }
                ],
            }
        ]
    """
    def get_onderwerpgroepen(self):
        raise NotImplementedError("You must implement get_onderwerpgroepen")

    """" afdelingen
        success": Boolean,
        "result": [
            {
                "code": String,
                "omschrijving": String
            }
        ]
    """
    def get_afdelingen(self):
        raise NotImplementedError("You must implement get_afdelingen")

    def get_afdeling_relaties(self):
        raise NotImplementedError("You must implement get_afdeling_relaties")

    def melding_aanmaken(self):
        raise NotImplementedError("You must implement melding_aanmaken")

    def afhandelen(self):
        raise NotImplementedError("You must implement afhandelen")
