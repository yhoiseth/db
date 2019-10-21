from django_heroku import settings

from .base import *  # noqa: F401, F403

DEBUG = False
settings(locals())
