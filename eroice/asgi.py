# Import the 'os' module to work with operating system functionalities
import os

# Import the 'get_asgi_application' function from Django's core asgi module
from django.core.asgi import get_asgi_application

# Set the 'DJANGO_SETTINGS_MODULE' environment variable to the project's settings module
# This tells Django which settings module to use for the application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eroice.settings')

# Get the ASGI application instance for the project
application = get_asgi_application()
