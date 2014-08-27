"""
Django settings for basetracker project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'we--!oph56^9!ys%1#t%@-pk&^lcfceuten7uc1rqy+8btt@dz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    #'applications.projects',
    #'applications.profiles',
    #'applications.teams',
    'bt',
    'south',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'social.apps.django_app.context_processors.backends',    
    'social.apps.django_app.context_processors.login_redirect',    
    'django.contrib.messages.context_processors.messages',     
    'django.contrib.auth.context_processors.auth',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',       
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'basetracker.middlewares.RequireLoginMiddleware',
)

ROOT_URLCONF = 'basetracker.urls'

WSGI_APPLICATION = 'basetracker.wsgi.application'

# Custom app/model order
ADMIN_REORDER = (
        ("default", ("default.association", "default.nonce", "default.usersocialauth")),
        ("auth", ("auth.User", "auth.Group")),
        ("applications", ("applications.Project", "applications.Team")),

)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'basetracker',
        'USER': 'root',
        'PASSWORD' : 'demo123',
        'HOST' : '127.0.0.1'
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC-6'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_SOCIAL_AUTH_AS_ADMIN_LOGIN = True

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

LOGIN_URL = '/admin/projects/'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/admin/projects/'

## Facebook
SOCIAL_AUTH_FACEBOOK_KEY = '1464510653816877'

SOCIAL_AUTH_FACEBOOK_SECRET =  '35df000b6a447e1f5cb0f97cbf251baa'

SOCIAL_AUTH_FACEBOOK_SCOPE = [
    'email',
    'user_friends',
    'friends_location',    
]