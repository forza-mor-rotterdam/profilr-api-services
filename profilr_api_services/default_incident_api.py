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
        """
        post login {
            username: String
            password: String
        }
        """
        raise NotImplementedError("You must implement login")

    def get_user_info(self):
        raise NotImplementedError("You must implement get_user_info")

    def get_list(self):
        """ 
        get list [
            {
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
                }
            }
        ]
        """
        raise NotImplementedError("You must implement get_list")

    def get_detail(self):
        """
        get detail {
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
        }
        """
        raise NotImplementedError("You must implement get_detail")

    def get_mutatieregels(self):
        """
        get mutatieregels {
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
        }
        """
        raise NotImplementedError("You must implement get_mutatieregels")

    def get_foto(self):
        raise NotImplementedError("You must implement get_foto")

    def get_wijken(self):
        """ 
        get wijken {
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
            ]
        }
        """
        raise NotImplementedError("You must implement get_foto")

    def get_onderwerpgroepen(self):
        """ 
        get onderwerpgroepen {
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
        }
        """
        raise NotImplementedError("You must implement get_onderwerpgroepen")

    def get_afdelingen(self):
        """" 
        get afdelingen {
            success": Boolean,
            "result": [
                {
                    "code": String,
                    "omschrijving": String
                }
            ]
        }
        """
        raise NotImplementedError("You must implement get_afdelingen")

    def get_afdeling_relaties(self):
        raise NotImplementedError("You must implement get_afdeling_relaties")

    def melding_aanmaken(self):
        raise NotImplementedError("You must implement melding_aanmaken")

    def afhandelen(self):
        """
        post afhandelen {
            "meldingId": Number,
            "behandelaar": String,
            "meldingType": String ("N", "O"),
            "redenAfhandelenNiet": String,
            "afhandelOpmerking": String,
            "straat": String,
            "huisnummer": String,
        }
        """
        raise NotImplementedError("You must implement afhandelen")
