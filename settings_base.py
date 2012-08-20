# Django settings for inventory.mirimus.com project.
import os.path
import logging
import urlparse

gettext = lambda s: s

ROOTDIR = os.path.dirname(os.path.realpath(__file__))

PROJECT_DIR = os.path.dirname(__file__)
PARENT_DIR = os.path.dirname(os.path.abspath(PROJECT_DIR))

def project_path(d):
    path = os.path.abspath(os.path.dirname(__file__))    
    return os.path.join(path, d)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Philip Kalinsky', 'philip.kalinsky@eloquentbits.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': '',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'USER': '',
        'PASSWORD': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False
USE_L10N = False

LANGUAGE_CODE = 'en'

ugettext = lambda s: s
LANGUAGES = (
  ('en', ugettext('English')),
)

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PARENT_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PARENT_DIR, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

ADMIN_TOOLS_MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'f6-880tex62*7s9ujgrzki$+7o29z9@n8f%v3c!*(d354b+&(&'

#admin_tools
ADMIN_TOOLS_MEDIA_URL = '/static/'
#ADMIN_TOOLS_MENU = 'report.admin.ReportsMenu'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    #'django.template.loaders.filesystem.load_template_source',
    #'django.template.loaders.app_directories.load_template_source',
    #'django.template.loaders.eggs.load_template_source',
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.messages.context_processors.messages",
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    #'context_processors.static_media',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'esq-currencies.urls'

TEMPLATE_DIRS = (
    project_path("templates"),
)

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admindocs',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.staticfiles',

    'sorl',
    'south',
    'django_extensions',
    'money',
)

DEFAULT_FROM_EMAIL = 'to be set in local_settings.py'
SERVER_EMAIL = 'to be set in local_settings.py'
EMAIL_SUBJECT_PREFIX = 'to be set in local_settings.py'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

STATIC_DOC_ROOT =  os.path.dirname(__file__) + '/static'

