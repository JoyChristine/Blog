import os

class Config:
    QUOTES_API='http://quotes.stormconsultancy.co.uk/{}.json'
    SQLALCHEMY_TRACK_MODIFICATIONS=True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://blogger:mypass@localhost/blog'
    SECRET_KEY = 'MODIFY'
    WTF_CSRF_ENABLED = False


    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT= 465
    MAIL_USE_TLS= False
    MAIL_USE_SSL=True
    MAIL_USERNAME= os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD= os.environ.get('MAIL_PASSWORD')
    
class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",)

        

class DevConfig(Config):
    DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}