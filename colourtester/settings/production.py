#
# Production settings
#

from .base import *

import os
import dj_database_url

env = os.environ.copy()
SECRET_KEY = env['SECRET_KEY']
ALLOWED_HOSTS = ['*']
DEBUG = False

# Update database configuration with $DATABASE_URL.
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Where collectstatic puts files
STATIC_ROOT = os.path.join(os.path.dirname(PROJECT_DIR), 'staticfiles')

# URL to use when referring to static files located in STATIC_ROOT.
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)