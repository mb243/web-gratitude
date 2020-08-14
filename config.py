import os
import secrets


class Config(object):
    DEBUG = True
    ENV = 'development'
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_bytes(32)
    WTF_CSRF_SECRET_KEY = os.environ.get('WTF_CSRF_SECRET_KEY') or secrets.token_bytes(32)
