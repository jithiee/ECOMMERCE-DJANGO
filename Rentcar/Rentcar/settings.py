"""
Django settings for Rentcar project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from dotenv import load_dotenv
load_dotenv() #take environment variable form .env
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRETKEY=os.getenv('SECRETKEY')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-{SECRETKEY}'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',   
    'Home',
    'accounts',
    'Admin_panel',
    'Booking',
    'crispy_forms',
    'crispy_bootstrap5',
    'fontawesomefree'
   
    
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Rentcar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'],
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

WSGI_APPLICATION = 'Rentcar.wsgi.application'
AUTH_USER_MODEL = 'accounts.Account'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME':'rent_car_db',
#         'USER':'postgres',
#         'PASSWORD':1598,
#         'HOST':'localhost',
       
       
#     }
# }   


POSTGRESPASSOWRD = os.getenv('POSTGRESPASSOWRD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'rentcars',
        'USER':'mysuperuser',
        'PASSWORD':POSTGRESPASSOWRD,
        'HOST':'rentcars.caz7kovkdc8n.us-east-1.rds.amazonaws.com',
       'PORT':'5432',
       
    }
}   



# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
   
    os.path.join(BASE_DIR,'static')
] 
MEDIA_URL ='media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.ERROR: "DANGER",
  
}

#SMTP comfigeration 

EMAILHOSTUSER=os.getenv('EMAILHOSTUSER')
EMAILHOSTPASSWORD=os.getenv('EMAILHOSTPASSWORD')

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT =  587
EMAIL_HOST_USER = EMAILHOSTUSER
EMAIL_HOST_PASSWORD = EMAILHOSTPASSWORD
EMAIL_USE_TLS = True



RAZORPAYKEY  =os.getenv('RAZORPAYKEY')
RAZORPAYSECRETKEY  =os.getenv('RAZORPAYSECRETKEY')

RAZORPAY_KEY = RAZORPAYKEY
RAZORPAY_SECRET_KEY  = RAZORPAYSECRETKEY


AWSACCESSKEYID=os.getenv('AWSACCESSKEYID')
AWSSECRETACCESSKEY=os.getenv('AWSSECRETACCESSKEY')


AWS_ACCESS_KEY_ID=AWSACCESSKEYID
AWS_SECRET_ACCESS_KEY=AWSSECRETACCESSKEY
AWS_STORAGE_BUCKET_NAME='backendrentcar'
AWS_S3_SIGNATURE_NAME='s3v4',
AWS_S3_REGION_NAME='us-east-1'
AWS_S3_FILE_OVERWRITE=False
AWS_DEFAULT_ACL =None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE ='storages.backends.s3boto3.S3Boto3Storage'