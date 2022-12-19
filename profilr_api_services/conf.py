from django.conf import settings


class Settings:

    @property
    def MSB_API_URL(self) -> str:
        return getattr(settings, "MSB_API_URL", "https://diensten-acc.rotterdam.nl")

    @property
    def PROFILR_API_URL(self) -> str:
        return getattr(settings, "PROFILR_API_URL", "https://api.profilr-acc.forzamor.nl")

    @property
    def MSB_API_URL_PRODUCTION(self) -> str:
        return getattr(settings, "MSB_API_URL_PRODUCTION", "https://diensten.rotterdam.nl")

    @property
    def MSB_ENABLE_AFDELING_RELATIES_ENDPOINT(self) -> bool:
        return getattr(settings, "MSB_ENABLE_AFDELING_RELATIES_ENDPOINT", False)

    @property
    def MSB_ENABLE_MELDING_AFHANDELEN(self) -> bool:
        if self.MSB_API_URL.startswith(self.MSB_API_URL_PRODUCTION):
            return False
        return getattr(settings, "MSB_ENABLE_MELDING_AFHANDELEN", False)


conf = Settings()