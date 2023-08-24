# Import the 'os' module to work with operating system functionalities
import os

# Import the 'get_wsgi_application' function from Django's core wsgi module
from django.core.wsgi import get_wsgi_application

# Set the 'DJANGO_SETTINGS_MODULE' environment variable to the project's settings module
# This tells Django which settings module to use for the application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eroice.settings')

# Get the WSGI application instance for the project
application = get_wsgi_application()
