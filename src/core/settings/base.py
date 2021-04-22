from pathlib import Path

WEBSITE_ROOT = Path(__file__).resolve().parent.parent.parent
PROJECT_ROOT = WEBSITE_ROOT.parent

SECRET_KEY = '{{ secret_key }}'

DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ORIGIN_ALLOW_ALL = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'drf_yasg',
    'django_filters',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    # 'django.contrib.sites',

    'accounts',
    'core',
]

AUTH_USER_MODEL = 'accounts.User'

# SITE_ID = 1

# AUTHENTICATION_BACKENDS = (
#     # allow non-active users to authenticate
#     'django.contrib.auth.backends.AllowAllUsersModelBackend',
#     # 'django.contrib.auth.backends.ModelBackend',
# )

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [WEBSITE_ROOT.joinpath('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "core.context_processors.debug",
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
# ASGI_APPLICATION = 'core.asgi.application'

{% with 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'|make_list as chars %}{% with a=chars|random b=chars|random c=chars|random d=chars|random e=chars|random f=chars|random g=chars|random h=chars|random i=chars|random j=chars|random k=chars|random l=chars|random m=chars|random n=chars|random o=chars|random p=chars|random %}# DATABASES = {
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ files.1 }}_db',
        'USER': '{{ files.1 }}_usr',
        'PASSWORD': '{{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}',
        'HOST': 'localhost',
        'PORT': 5432
    }
}
"""
sudo -u postgres psql -c "CREATE DATABASE {{ files.1 }}_db;"
sudo -u postgres psql -c "CREATE USER {{ files.1 }}_usr with password '{{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE {{ files.1 }}_db to {{ files.1 }}_usr;"
sudo -u postgres psql -c "ALTER USER {{ files.1 }}_usr CREATEDB;"  # for tests
"""{% endwith %}{% endwith %}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LOG_PATH = PROJECT_ROOT.joinpath("logs")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'django_error': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': LOG_PATH.joinpath('django.log'),
        },
        'mail_devs': {
            'class': 'core.handlers.SendEmailToDevelopersHandler',
            'level': 'ERROR',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['django_error', 'mail_devs'],
            'level': 'WARNING',
            'propagate': True,
        },
    }
}


LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_ROOT.joinpath('static_root')

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_ROOT.joinpath('media_root')


REST_FRAMEWORK = {
    # 'DEFAULT_PERMISSION_CLASSES': (
    #     'rest_framework.permissions.IsAuthenticated',
    # ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        # 'rest_framework.filters.SearchFilter',
        # 'rest_framework.filters.OrderingFilter',
    ),
    'EXCEPTION_HANDLER': 'core.drf_exception_handler_overide.exception_handler_override',
    'NON_FIELD_ERRORS_KEY': 'error',
}

FILE_UPLOAD_MAX_MEMORY_SIZE = 1000000000
FILE_UPLOAD_PERMISSIONS = 0o644

{% with 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'|make_list as chars %}{% with a=chars|random b=chars|random c=chars|random d=chars|random e=chars|random f=chars|random g=chars|random h=chars|random i=chars|random j=chars|random k=chars|random l=chars|random m=chars|random n=chars|random o=chars|random p=chars|random %}
# BROKER_URL = 'amqp://{{ files.1 }}:{{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}@localhost:5672/{{ files.1 }}_vhost'
"""
sudo rabbitmqctl add_user {{ files.1 }} {{a}}{{b}}{{c}}{{d}}{{e}}{{f}}{{g}}{{h}}{{i}}{{j}}{{k}}{{l}}{{m}}{{n}}{{o}}{{p}}
sudo rabbitmqctl add_vhost {{ files.1 }}_vhost
sudo rabbitmqctl set_permissions -p {{ files.1 }}_vhost {{ files.1 }} ".*" ".*" ".*"

# in case "something went wrong"
sudo rabbitmqctl stop_app
sudo rabbitmqctl reset
sudo rabbitmqctl start_app
""" {% endwith %}{% endwith %}
