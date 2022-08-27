from django.apps import AppConfig


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'User'
    
    #connect the receiver in the ready method
    def ready(self):
        import User.signals