# -*- coding: UTF-8 -*-
from settings_base import *

LOCAL_DEV = True
DEBUG = True
TEMPLATE_DEBUG = DEBUG

if LOCAL_DEV:
    INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'NAME': 'esq-currencies',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'web',
        'PASSWORD': 'web',
        'HOST': '127.0.0.1',
    }
}


DEFAULT_FROM_EMAIL = 'no-reply@esq-group.com'
SERVER_EMAIL = 'alerts@esq-group.com'
EMAIL_SUBJECT_PREFIX = 'esq-group.com [Django] '


LOGFILE = "esq-currencies.log"
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(ROOTDIR, '../log', LOGFILE),
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter':'standard',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'request_handler': {
                'class':'django.utils.log.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.db.backends': { # Stop SQL debug from logging to main logger
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}





