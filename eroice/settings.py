from pathlib import Path

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Set the secret key for the Django application (for production use, use environment variables)
SECRET_KEY = "django-insecure-iten-d_h)j#*ldvc9jhw44e22iw!yb2gv$ysr*xuss(v4*^tjn"

# Set the debugging mode (True for development, False for production)
DEBUG = False

# List of allowed hostnames for the application
ALLOWED_HOSTS = ["eroice.ictman4jkt.com", "127.0.0.1", "localhost"]

# List of installed applications in the Django project
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "eroice",  # Your app(s) should be included here
    "import_export",
]

# List of middleware classes used for processing HTTP requests and responses
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Specify the root URL configuration for the project
ROOT_URLCONF = "eroice.urls"

# Configuration settings for template rendering
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# WSGI application configuration
WSGI_APPLICATION = "eroice.wsgi.application"

# Database configuration settings
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # SQLite database file
    }
}

# Configuration for password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Language and timezone settings
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"

# Internationalization settings
USE_I18N = True
USE_TZ = True

# Configuration for serving static files
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"

# Static files storage using Whitenoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Email configuration settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
DEFAULT_FROM_EMAIL = "eroice.id@gmail.com"
SERVER_EMAIL = "eroice.id@gmail.com"
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "eroice.id@gmail.com"
EMAIL_HOST_PASSWORD = "••••••••"  # Use your actual email password here
