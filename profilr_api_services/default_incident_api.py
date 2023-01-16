from .base import APIService


class IncidentAPIService(APIService):
    def validate_filters(self):
        raise NotImplementedError("You must implement validate_filters")

    def logout(self):
        raise NotImplementedError("You must implement logout")

    def login(self):
        raise NotImplementedError("You must implement login")

    def get_user_info(self, user_token):
        raise NotImplementedError("You must implement get_user_info")

    def get_list(self):
        raise NotImplementedError("You must implement get_list")

    def get_detail(self):
        raise NotImplementedError("You must implement get_detail")

    def get_mutatieregels(self):
        raise NotImplementedError("You must implement get_mutatieregels")

    def get_foto(self):
        raise NotImplementedError("You must implement get_foto")

    def get_wijken(self):
        raise NotImplementedError("You must implement get_foto")

    def get_onderwerpgroepen(self):
        raise NotImplementedError("You must implement get_onderwerpgroepen")

    def get_afdelingen(self):
        raise NotImplementedError("You must implement get_afdelingen")

    def get_afdeling_relaties(self):
        raise NotImplementedError("You must implement get_afdeling_relaties")

    def melding_aanmaken(self):
        raise NotImplementedError("You must implement melding_aanmaken")

    def afhandelen(self):
        raise NotImplementedError("You must implement afhandelen")
