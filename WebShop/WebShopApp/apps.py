from django.apps import AppConfig


class WebshopappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'WebShopApp'
    def ready(self):
        import WebShopApp.signals