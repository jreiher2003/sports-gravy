import os

class BaseConfig(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ['SECRET_KEY']
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_DATABASE_URI = "sqlite:///sports.db"
    CACHE_TYPE = "memcached"
    BCRYPT_LOG_ROUNDS = 12
    MAIL_SERVER = os.environ["MAIL_SERVER"]
    MAIL_PORT = os.environ["MAIL_PORT"]
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = os.environ["MAIL_USERNAME"]
    MAIL_PASSWORD = os.environ["MAIL_PASSWORD"]
    MAIL_DEFAULT_SENDER = '"Site Admin" <noreply@sports-gravy.com>'

    SECURITY_UNAUTHORIZED_VIEW = "/nfl/"
    SECURITY_MSG_UNAUTHORIZED = ("You don't have permission to go there", "danger")

    OCP_APIM_SUBSCRIPTION_KEY = os.environ["OCP_APIM_SUBSCRIPTION_KEY"]

    UPLOADED_PHOTOS_DEST = '/tmp/photolog/photos'
    # UPLOADS_DEFAULT_DEST = "app/static/"
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    MAIL_SUPPRESS_SEND = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    

class ProductionConfig(BaseConfig):
    DEBUG = False