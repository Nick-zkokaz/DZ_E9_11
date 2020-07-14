import os

class Config():
    FLASK_DEBUG = False
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = os.getenv('PORT', 5000)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'e#!xkhudyp^e4^ht0_tiwh7nn9n0oo8!%qftg2s8m5k%x6t1j&')
