import os

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Som3$ec5etK*y'
    UPLOAD_PROFILE = os.environ['UPLOAD_PROFILE'] = './app/staticuploads/profile' 
    UPLOAD_CARPHOTO = os.environ['UPLOAD_CARPHOTO'] = './app/static/uploads/carPhoto' 
    UPLOAD_VPROFILE = os.environ['UPLOAD_VPROFILE'] = 'static/uploads/profile' 
    UPLOAD_VCARPHOTO = os.environ['UPLOAD_VCARPHOTO'] = 'static/uploads/carPhoto'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://znumtfhciuflgi:d301b7fc3b692b3090f998668556087f25ce7ba07032c3632e6e554eb477b847@ec2-54-90-211-192.compute-1.amazonaws.com:5432/d78kmplhv5g4ht'
    #'postgresql://project2:mkm2021@localhost/project2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """Development Config that extends the Base Config Object"""
    DEVELOPMENT = True
    DEBUG = True

class ProductionConfig(Config):
    """Production Config that extends the Base Config Object"""
    DEBUG = False