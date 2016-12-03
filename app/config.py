import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    WTF_CSRF_ENABLED = False
    SECRET_KEY = 'Se, cr, et!'
    SQLALCHEMY_DATABASE_URI = "postgresql:///a_attendance"
    SITE_WIDTH = 800

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True