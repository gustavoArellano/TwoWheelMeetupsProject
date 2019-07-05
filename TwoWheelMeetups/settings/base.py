import os
from decouple import config

BOOTSTRAP4 = {
    'include_jquery': True,
}

BASE_DIR = os.path.dirname(
            os.path.dirname(    
            os.path.dirname(
            os.path.abspath(__file__))))


SECRET_KEY = config('SECRET_KEY')
API_KEY = config('API')

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'apps.MainApp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap_datepicker_plus'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TwoWheelMeetups.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'TwoWheelMeetups.wsgi.application'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'MainApp')

MEDIA_ROOT = '/Users/gustavo/Documents/Projects/Python/TwoWheelMeetups/apps/MainApp/media/'
MEDIA_URL = '/Users/gustavo/Documents/Projects/Python/TwoWheelMeetups/apps/MainApp/media/RiderImages/'



