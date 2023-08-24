from django.apps import AppConfig

# Configuration class for the 'eroice' app
class EroiceConfig(AppConfig):
    # Use BigAutoField as the default primary key
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specify the app's name as 'eroice'
    name = 'eroice'
    
    # Define the 'ready' method that is executed when the app is ready
    def ready(self):
        # Import the signals module to ensure signal handling is set up
        import eroice.signals
