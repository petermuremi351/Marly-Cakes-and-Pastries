
# from pathlib import Path
# import os
# from dotenv import load_dotenv
# from decouple import config




# MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
# MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
# MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE", "174379")
# MPESA_ENVIRONMENT = os.getenv("MPESA_ENVIRONMENT", "sandbox")
# MPESA_CALLBACK_URL = os.getenv("MPESA_CALLBACK_URL")

# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR = Path(__file__).resolve().parent.parent
# # load our environmental variables
# # load_dotenv()

# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-yps4k5246nnw%j%bao6!l**!69f0c42wa8jo9*q5)l^5a(wy47'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


# ALLOWED_HOSTS = [
#     "doretta-unpulverable-eldora.ngrok-free.dev",
#     "localhost",
#     "127.0.0.1"
# ]

# CSRF_TRUSTED_ORIGINS = [
#     "https://doretta-unpulverable-eldora.ngrok-free.dev",
# ]



# # Application definition

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'store',
#     'cart',
#     'payment',
#     'paypal.standard.ipn',
#     'django_daraja',
    
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     # 'whitenoise.middleware.WhiteNoiseMiddleware'
# ]

# ROOT_URLCONF = 'MarlyCakesPastries.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'cart.context_processors.cart',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'MarlyCakesPastries.wsgi.application'


# # Database
# # https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',

#     }
# }


# # Password validation
# # https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# # Internationalization
# # https://docs.djangoproject.com/en/6.0/topics/i18n/

# LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'

# USE_I18N = True

# USE_TZ = True


# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/6.0/howto/static-files/

# STATIC_URL = 'static/'
# STATICFILES_DIRS = ['static/']

# # White noise static stuff
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATIC_ROOT = BASE_DIR / 'staticfiles'

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # add paypal settings
# # set sendbox to True

# PAYPAL_TEST = True

# PAYPAL_RECEIVER_EMAIL = 'businessmarlyi@gmail.com'


# # The Mpesa environment to use
# # Possible values: sandbox, production

# MPESA_ENVIRONMENT = 'sandbox'

# # Credentials for the daraja app

# MPESA_CONSUMER_KEY = 'mpesa_consumer_key'
# MPESA_CONSUMER_SECRET = 'mpesa_consumer_secret'

# #Shortcode to use for transactions. For sandbox  use the Shortcode 1 provided on test credentials page

# MPESA_SHORTCODE = 'mpesa_shortcode'

# # Shortcode to use for Lipa na MPESA Online (MPESA Express) transactions
# # This is only used on sandbox, do not set this variable in production
# # For sandbox use the Lipa na MPESA Online Shorcode provided on test credentials page

# MPESA_EXPRESS_SHORTCODE = 'mpesa_express_shortcode'

# # Type of shortcode
# # Possible values:
# # - paybill (For Paybill)
# # - till_number (For Buy Goods Till Number)

# MPESA_SHORTCODE_TYPE = 'paybill'

# # Lipa na MPESA Online passkey
# # Sandbox passkey is available on test credentials page
# # Production passkey is sent via email once you go live

# MPESA_PASSKEY = 'mpesa_passkey'

# # Username for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

# MPESA_INITIATOR_USERNAME = 'initiator_username'

# # Plaintext password for initiator (to be used in B2C, B2B, AccountBalance and TransactionStatusQuery Transactions)

# MPESA_INITIATOR_SECURITY_CREDENTIAL = 'initiator_security_credential'




from pathlib import Path
import os
from dotenv import load_dotenv
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environmental variables
load_dotenv()

# M-Pesa settings from .env
MPESA_CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY")
MPESA_CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET")
MPESA_SHORTCODE = os.getenv("MPESA_SHORTCODE", "174379")
MPESA_ENVIRONMENT = os.getenv("MPESA_ENVIRONMENT", "sandbox")
MPESA_CALLBACK_URL = os.getenv("MPESA_CALLBACK_URL")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-yps4k5246nnw%j%bao6!l**!69f0c42wa8jo9*q5)l^5a(wy47'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "doretta-unpulverable-eldora.ngrok-free.dev",
    "localhost",
    "127.0.0.1"
]

CSRF_TRUSTED_ORIGINS = [
    "https://doretta-unpulverable-eldora.ngrok-free.dev",
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'cart',
    'payment',
    'paypal.standard.ipn',
    'django_daraja',
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

ROOT_URLCONF = 'MarlyCakesPastries.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'MarlyCakesPastries.wsgi.application'

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation

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

# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

# Static files

STATIC_URL = 'static/'
STATICFILES_DIRS = ['static/']

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# PayPal settings

PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL = 'businessmarlyi@gmail.com'

# Additional M-Pesa settings required by django_daraja

MPESA_EXPRESS_SHORTCODE = MPESA_SHORTCODE
MPESA_SHORTCODE_TYPE = 'paybill'
MPESA_PASSKEY = os.getenv("MPESA_PASSKEY")

MPESA_INITIATOR_USERNAME = os.getenv("MPESA_INITIATOR_USERNAME")
MPESA_INITIATOR_SECURITY_CREDENTIAL = os.getenv("MPESA_INITIATOR_SECURITY_CREDENTIAL")