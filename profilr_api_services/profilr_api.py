from .default_profile_api import DefaultProfileApi
from .conf import conf


class ProfilrApi(DefaultProfileApi):
    _json_enabled = True

    def set_profile(self, user_token, data):
        return self.do_request(
            "profile/", user_token, method=ProfilrApi.POST, data=data, no_cache=True
        ).json()

    def get_profile(self, user_token):
        return self.do_request("profile/", user_token, no_cache=True).json()
