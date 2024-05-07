import os
from pathlib import Path
# from django.utils.translation import gettext_lazy as _


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5g0wg%huyd)-pldwtn)4a1#0p+*4xrtiv&lar=00-ug%xb+k8n'

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
    # 'modeltranslation',
    'orders',
    'social_django',
    'product',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',
    
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware' ,

]

ROOT_URLCONF = 'store.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'product.context_processors.baskets',
            ],
        },
    },
]

WSGI_APPLICATION = 'store.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
STATICFILES_DIRS  = [os.path.join(BASE_DIR, 'static/')]


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field


AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    
    # 'social_core.backends.instagram.InstagramOAuth2',
    # 'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',




]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='127646207839-e3v9jihjbkp5jm0nvub8lmj9scnfguj4.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_REDIRECT_URI = 'http://localhost:8000/social_auth/complete/google-oauth2/'

STRIPE_PUBLIC_KEY = 'pk_test_51OhqLhHVlKmVyU1GvoALwxH56HjjWXdZrQTh786UZ57ZXuK70vuZAlJthZ9rQmB6RKkQjXSWsLvVwgQdJhV7r6Zc00oiSpXVJM'
STRIPE_SECRET_KEY = 'sk_test_51OhqLhHVlKmVyU1G6MogldJlJmVrrEb4y3XQO4p9SCbYW3kTdVa4aD9jr1VwiDa82V7dGEwJNbMo2J96atr48DoT00hZebdw6i'
 # add this
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
#   'fields': 'id, name, email, picture.type(large), link'
# }
# SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [                 # add this
#     ('name', 'name'),
#     ('email', 'email'),
#     ('picture', 'picture'),
#     ('link', 'profile_url'),
# ]



LOGIN_URL= 'login'
LOGIN_REDIRECT_URL= 'index'
#languages
# LANGUAGES = [
#     ("uz", _("Uzbek")),
#     ("ru", _("Russian")),
#     ("en", _("English")),
   
# ]

# MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'

# LOCALE_PATHS = (BASE_DIR, 'locale/')