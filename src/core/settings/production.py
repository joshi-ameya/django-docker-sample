"""
Production env settings.
"""
import os
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'false').lower() == "true"
# DEBUG = True
# DEFAULT_CONNECTION = dj_database_url.parse(
#     os.environ.get("DATABASE_URL_CONFIG"))
# DEFAULT_CONNECTION = dj_database_url.parse(
#     "postgres://postgres:ameya1993@database-2.ct1zyytqf3gw.us-east-2.rds.amazonaws.com:5432/sharebucktest")
# DEFAULT_CONNECTION.update({"CONN_MAX_AGE": 600})
# DATABASES = {"default": DEFAULT_CONNECTION}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_NAME"),
        'USER': os.environ.get("POSTGRES_USER"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        # 'PORT': '5432',
        'ATOMIC_REQUESTS': True
    }
}

ALLOWED_HOSTS = ['*']


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
