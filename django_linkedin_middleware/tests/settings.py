import os

BASE_DIR = os.path.dirname(__file__)
SECRET_KEY = 'some_secret_key'
DEBUG = True
ALLOWED_HOSTS = []
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
)

LINKEDIN_APPLICATION_KEY = ""
LINKEDIN_APPLICATION_SECRET = ""
LINKEDIN_APPLICATION_RETURN_CALLBACK = ""
LINKEDIN_APPLICATION_PROFILE = ['r_basicprofile']
PAGES_WITH_LINKEDIN_AUTH_REQUIRED = ['*']
PAGES_WITHOUT_LINKEDIN_AUTH_REQUIRED = []
