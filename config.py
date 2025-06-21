import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin02:hotelku1234@localhost/hotelku'
    SQLALCHEMY_TRACK_MODIFICATIONS = False