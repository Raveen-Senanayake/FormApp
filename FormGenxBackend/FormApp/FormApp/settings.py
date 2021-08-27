"""
Django settings for FormApp project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', False)
DEBUG_PROPAGATE_EXCEPTIONS = os.environ.get('DEBUG_PROPAGATE_EXCEPTIONS', False)
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(',')

# Application additions
AUTH_USER_MODEL = 'user.User'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = os.environ.get('ACCOUNT_EMAIL_CONFIRMATION_REDIRECT_URL', '/login/')
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL = os.environ.get('ACCOUNT_EMAIL_CONFIRMATION_REDIRECT_URL', '/login/')
OLD_PASSWORD_FIELD_ENABLED = True
NOTIFICATIONS_EMAIL_ADDRESS = os.environ.get('NOTIFICATIONS_EMAIL_ADDRESS', "iStaffNotifications@gmail.com")
MONGODB_URI = os.environ.get('MONGODB_URI',"mongodb+srv://Raveen:8VBCDyi6BkL3vh@cluster0.dj3sr.mongodb.net/formdatabase?retryWrites=true&w=majority")
SITE_ID = 1

JOB_STILL_VIEWABLE_OFFSET = 4 # We should be able to see a job up to 4 hours after it has passed.



# Email Backend Configuration
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', True)
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',


    # Rest Framework
    'rest_framework',
    'rest_framework.authtoken',

    ##ourapps
    'creator.apps.CreatorConfig',
    'form.apps.FormConfig',
    'formuser.apps.FormuserConfig',
    'user.apps.UserConfig',

 # Auth
    'rest_auth',
    'corsheaders',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', False)

REST_AUTH_SERIALIZERS = {
    'TOKEN_SERIALIZER': 'user.serializers.TokenSerializer',
}

REST_FRAMEWORK = {
    # Default endpoints to look like JSON in production but not in development.
    'DEFAULT_RENDERER_CLASSES': (
        os.environ.get('DEFAULT_RENDERER_CLASS', 'rest_framework.renderers.JSONRenderer'),
    ),
    # Authenticate using token auth.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

AUTHENTICATION_BACKEND = ["django.contrib.auth.backends.ModelBackend","sesame.backends.ModelBackend"]


# # settings.py
# MAGIC_LINK = {
#     # link expiry, in seconds
#     "DEFAULT_EXPIRY": 300,
#     # default link redirect
#     "DEFAULT_REDIRECT": "/",
#     # the preferred authorization backend to use, in the case where you have more
#     # than one specified in the `settings.AUTHORIZATION_BACKENDS` setting.
#     "AUTHENTICATION_BACKEND": "django.contrib.auth.backends.ModelBackend",
#     # SESSION_COOKIE_AGE override for magic-link logins - in seconds (default is 1 week)
#     "SESSION_EXPIRY": 7 * 24 * 60 * 60
# }


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware', 

    'django.middleware.security.SecurityMiddleware',
    

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware' ,
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'



]



ROOT_URLCONF = 'FormApp.urls'
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/login/'

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

WSGI_APPLICATION = 'FormApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': {
            'host': 'mongodb+srv://Raveen:8VBCDyi6BkL3vh@cluster0.dj3sr.mongodb.net/formdatabase?retryWrites=true&w=majority',
            'username': 'Raveen',
            'password': '8VBCDyi6BkL3vh',
            'authMechanism': 'SCRAM-SHA-1'
        }
    }
}
# DATABASES = {
#         'default': {
#             'ENGINE': 'djongo',
            
#             'Client': { 
#            "host": "mongodb+srv://Raveen:8VBCDyi6BkL3vh@cluster0.dj3sr.mongodb.net/formdatabase?retryWrites=true&w=majority",
#            "username": 'Raveen',
#            "password": '8VBCDyi6BkL3vh',
#            "authMechanism": "SCRAM-SHA-1", 
#             },
#         }
#     }
#     DATABASES = {
#     'default': {
#         'ENGINE': 'djongo',
#         'CLIENT': {
#             'host': 'mongodb+srv://Raveen:8VBCDyi6BkL3vh@cluster0.dj3sr.mongodb.net/formdatabase?retryWrites=true&w=majority',
#             'username': 'Raveen',
#             'password': '8VBCDyi6BkL3vh',
#             'authMechanism': 'SCRAM-SHA-1'
#         }
#     }
# }

AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

# AUTHENTICATION_BACKENDS = (xsxs
#     'mongoengine.django.auth.MongoEnginexsBackend',
# )
# SESSION_ENGINE = 'mongoengine.django.sessions'
# # SESSION_SERIALIZER = 'mongoengine.django.sessions.BSONSerializer'

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

if os.environ.get('CORS_ALLOWED_ORIGIN_REGEXES'):
    # To Regex an environment variable, we must first convert them to a raw string.
    CORS_ALLOWED_ORIGIN_REGEXES = [ r"{0}".format(allowed_origin) for allowed_origin in os.environ.get('CORS_ALLOWED_ORIGIN_REGEXES').split(',')  ]

if os.environ.get('CORS_ALLOWED_ORIGINS'):
    CORS_ALLOWED_ORIGINS = os.environ.get('CORS_ALLOWED_ORIGINS').split(',')

g
# Internationalization

# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
