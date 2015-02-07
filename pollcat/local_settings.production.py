import os.path

import os
PATH = os.path.abspath(os.path.dirname(__file__))


def relative(path):
    return os.path.abspath(os.path.join(PATH, path))

BUCKET_NAME = "pollcat"

DEBUG = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False

MEDIA_ROOT = relative('media')

MEDIA_URL = "/uploads/"

STATIC_ROOT = ''

STATIC_URL = 'https://pollcat.s3.amazonaws.com/'


DEVELOPMENT = False

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = False # Don't include auth in every url
AWS_STORAGE_BUCKET_NAME = BUCKET_NAME

EMAIL_BACKEND = 'django_ses.SESBackend'
SERVER_EMAIL = 'no-reply@pollcat.ca'

#django-contact-form
DEFAULT_FROM_EMAIL = 'contactform@pollcat.ca'

MANAGERS = (
    ('Web Manager', 'manager@pollcat.ca'),
)

ADMINS = (
    ('Web Admin','admin@pollcat.ca'),
)

try:
    from secure_settings import *
except ImportError:
    pass