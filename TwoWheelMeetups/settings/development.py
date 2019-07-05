from .base import *

DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS += []

MIDDLEWARE += []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# # For Development Only
# # MEDIA_ROOT is for server path to store files in the computer.
# MEDIA_ROOT =  os.path.join(BASE_DIR, '/TwoWheelMeetups/media') 
# # MEDIA_URL is the reference URL for browser to access the files over Http.
# MEDIA_URL = '/media/'