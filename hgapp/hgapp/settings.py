"""
Django settings for hgapp project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import pytz

try:
    os.environ['SECRET_KEY']
    DEBUG = False
except:
    DEBUG = True

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = PROJECT_ROOT

if DEBUG:
    ALLOWED_HOSTS = [
        '127.0.0.1',
        'localhost'
    ]
else:
    ALLOWED_HOSTS = [
        'hgapp-dev.us-west-2.elasticbeanstalk.com',
        'thecontractgame.com',
        'www.thecontractgame.com',
        'thecontractrpg.com',
        'www.thecontractrpg.com',
        'contract-al2-hgapp.wrumqdjmpw.us-west-2.elasticbeanstalk.com',
        'hgapp-env-contract.wrumqdjmpw.us-west-2.elasticbeanstalk.com',
        'hgapp-env-1.wrumqdjmpw.us-west-2.elasticbeanstalk.com',
    ]
    SESSION_COOKIE_DOMAIN = ".thecontractrpg.com"

INTERNAL_IPS = (
    '127.0.0.1',
    '192.168.1.23',
)

SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"
# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"

#TODO: figure out a place to deployably serve our static files from that doesn't serve source
STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
]

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"

# List of finder classes that know how to find static files in
# various locations.

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

FILE_UPLOAD_HANDLERS = [
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler"
]
if DEBUG and 'AWS_ACCESS_KEY_ID' not in os.environ:
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media-root')
else:
    AWS_DEFAULT_ACL = None
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    AWS_QUERYSTRING_AUTH = False
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_REGION_NAME = os.environ['AWS_S3_REGION_NAME']


# SECURITY WARNING: keep the secret key used in production secret!
if DEBUG:
    SECRET_KEY = '(35@*@4v-wy68tnjx*8pfzk4al=5pwa(2yaur=eoeqa8f@mb#c'
else:
    SECRET_KEY = os.environ['SECRET_KEY']

# Official webhooks
if DEBUG:
    LFG_WEBHOOK_URL = 'https://discord.com/api/webhooks/911653506384011314/4yUXGA8Q1qhrXaxMNBYI1cIYcfyTyNbKS87NFqVA05VMrw9KOcGnjsaWai9byI8Yj0r_'
    NEWBIE_WEBHOOK_URL = 'https://discord.com/api/webhooks/911653506384011314/4yUXGA8Q1qhrXaxMNBYI1cIYcfyTyNbKS87NFqVA05VMrw9KOcGnjsaWai9byI8Yj0r_'
else:
    LFG_WEBHOOK_URL = os.environ['LFG_WEBHOOK_URL']
    NEWBIE_WEBHOOK_URL = os.environ['NEWBIE_WEBHOOK_URL']


# Application definition

INSTALLED_APPS = [
    'powers.apps.PowersConfig',
    'profiles.apps.ProfilesConfig',
    'characters.apps.CharactersConfig',
    'games.apps.GamesConfig',
    'overrides.apps.OverridesConfig',
    'cells.apps.CellsConfig',
    'info.apps.InfoConfig',
    'journals.apps.JournalsConfig',
    'guide.apps.GuideConfig',
    'crafting.apps.CraftingConfig',
    'emails.apps.EmailsConfig',
    'images.apps.ImagesConfig',
    'notifications.apps.NotificationsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # external
    "account",
    "pinax.eventlog",
    'guardian',
    'pagedown.apps.PagedownConfig',
    'markdown_deux',
    'postman',
    'tinymce',
    "blog",
    "pinax.images",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'hgapp.middleware.TimezoneMiddleware'
]

if DEBUG:
    pass
    # COMMENT BELOW TO DISABLE DEBUG TOOLBAR
    # INSTALLED_APPS.append("debug_toolbar")
    # MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    # RESULTS_CACHE_SIZE=4000

ACCOUNT_REMEMBER_ME_EXPIRY = 60 * 60 * 24 * 365 * 10
SESSION_COOKIE_AGE = ACCOUNT_REMEMBER_ME_EXPIRY
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"

ROOT_URLCONF = 'hgapp.urls'
CSRF_FAILURE_VIEW = 'hgapp.views.csrf_failure'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            "debug": DEBUG,
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "postman.context_processors.inbox",
            ],
        },
    },
]

WSGI_APPLICATION = 'hgapp.wsgi.application'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {name} {message}',
            'style': '{',
        },
        'verbose_ses': {
            'format': '{levelname} {asctime} {name} {message} {notification}',
            'style': '{',
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'applogfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'contract-app.log'),
            'maxBytes': 1024*1024*15, # 15MB
            'backupCount': 1,
            'formatter': 'verbose'
        },
        'applogfile_ses': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'contract-app.log'),
            'maxBytes': 1024 * 1024 * 15,  # 15MB
            'backupCount': 1,
            'formatter': 'verbose_ses'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'applogfile'],
        },
        'django.request': {
            'handlers': ['mail_admins', 'applogfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.security': {
            'handlers': ['mail_admins', 'applogfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'py.warnings': {
            'handlers': ['console', 'applogfile'],
            'propagate': True,
        },
        'app': {
            'handlers': ['console', 'applogfile'],
            'level': os.getenv('APP_LOG_LEVEL', default='INFO'),
            'propagate': True,
        },
        'django_ses': {
            'handlers': ['console', 'applogfile_ses'],
            'level': os.getenv('APP_LOG_LEVEL', default='INFO'),
            'propagate': True,
        },
    }
}

ADMINS = [('Spencer', 'spencerstecko@gmail.com'),]

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
if 'RDS_HOSTNAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
elif 'LOCAL_CONTRACT_POSTGRES' in os.environ:
    print("Using local postgres")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'contract',
            'USER': 'spencerstecko',
            'PASSWORD': 'password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
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

if DEBUG:
    DEFAULT_HTTP_PROTOCOL = "http"
else:
    DEFAULT_HTTP_PROTOCOL = "https"

# Caching
if DEBUG:
    pass
    # #Comment this CACHES block out to test caching during development.
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
else:
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '127.0.0.1:11211',
        }
    }

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SITE_ID = int(os.environ.get("SITE_ID", 1))

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

if DEBUG:
    if 'AWS_ACCESS_KEY_ID' in os.environ:
        DEFAULT_FROM_EMAIL = 'The Contract RPG <admin@thecontractrpg.com>'
        EMAIL_USE_TLS = True
        EMAIL_BACKEND = 'django_ses.SESBackend'
        AWS_SES_REGION_NAME = 'us-west-2'
        AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
    else:
        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    DEFAULT_FROM_EMAIL = 'The Contract RPG <admin@thecontractrpg.com>'
    EMAIL_USE_TLS = True
    EMAIL_BACKEND = 'django_ses.SESBackend'
    AWS_SES_REGION_NAME = 'us-west-2'
    AWS_SES_REGION_ENDPOINT = 'email.us-west-2.amazonaws.com'
    AWS_SES_CONFIGURATION_SET = "bounced-emails"
    SERVER_EMAIL = 'The Contract RPG <admin@thecontractrpg.com>'


def do_nothing(deletion):
    pass

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True
ACCOUNT_DELETION_EXPUNGE_CALLBACK = do_nothing
ACCOUNT_TIMEZONES = list(zip(pytz.common_timezones, pytz.common_timezones))
LOGIN_URL = '/account/login/'


AUTHENTICATION_BACKENDS = [
    "account.auth_backends.UsernameAuthenticationBackend",
    'guardian.backends.ObjectPermissionBackend',
]

#Postman settings
POSTMAN_DISALLOW_ANONYMOUS = True
POSTMAN_AUTO_MODERATE_AS = True
POSTMAN_NOTIFIER_APP = "emails.postman"

#Pagedown settings
PAGEDOWN_WIDGET_CSS = ("overrides/pagedown_widget.css",)


# Theme settings
THEME_CONTACT_EMAIL = "TheContractGame@gmail.com"

# TinyMCE settings
TINYMCE_JS_URL = "https://cdn.tiny.cloud/1/12xkz9g5ryiyz78mjzhthvq62r42rsi6tzik4yulk1tol6rn/tinymce/5/tinymce.min.js"
TINYMCE_DEFAULT_CONFIG = {
    "theme": "silver",
    "height": 500,
    "menubar": False,
    "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
    "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
    "code,help,wordcount",
    "toolbar": "formatselect fontselect fontsizeselect | "
    "bold italic strikethrough underline removeformat | backcolor forecolor | alignleft aligncenter "
    "| bullist numlist link unlink | image "
    " | help",
    'content_css': "/static/css/site.css",
    "font_formats":  "Andale Mono=andale mono,times; Arial=arial,helvetica,sans-serif; Arial Black=arial black,avant garde;"
                     " Book Antiqua=book antiqua,palatino; Comic Sans MS=comic sans ms,sans-serif; Courier New=courier "
                     "new,courier; Georgia=georgia,palatino; Helvetica=helvetica; Impact=impact,chicago; Symbol=symbol; "
                     "Tahoma=tahoma,arial,helvetica,sans-serif; Terminal=terminal,monaco; Times New Roman=times new roman,times; "
                     "Trebuchet MS=trebuchet ms,geneva; Verdana=verdana,geneva; "
                     "Alex Brush=Alex Brush; Aladin=Aladin; Annie Use Your Telescope=Annie Use Your Telescope; "
                     "Beth Ellen=Beth Ellen; Cedarville Cursive=Cedarville Cursive; Spirax=Spirax; Yomogi=Yomogi; "
                     "Rock Salt=Rock Salt; Webdings=webdings; Wingdings=wingdings,zapf dingbats"
}

# Pinax Blog settings
PINAX_BLOG_SLUG_UNIQUE = True