#
# DEV Settings
#

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3g0o_dh%ku!yb&80&x)o$gjtbd%)^*3dsdgvdfeu(e$pkscmpi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"), # project 
]

ALLOWED_HOSTS = ['*']