from django_heroku import settings

from .base import *  # noqa: F401, F403

DEBUG = False
COMPRESS_OFFLINE = True
LIBSASS_OUTPUT_STYLE = "compressed"
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
settings(locals())
