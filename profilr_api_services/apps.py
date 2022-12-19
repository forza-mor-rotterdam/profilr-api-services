from django.apps import AppConfig


class ServicesConfig(AppConfig):
    name = "profilr_api_services"
    verbose_name = "ProfilR API Services"

    def ready(self) -> None:

        return super().ready()
