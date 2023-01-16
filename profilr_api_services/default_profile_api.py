from .base import APIService
from .conf import conf


class DefaultProfileApi(APIService):
    def set_profile(self):
        raise NotImplementedError("You must implement set_profile")

    def get_profile(self):
        raise NotImplementedError("You must implement get_profile")

