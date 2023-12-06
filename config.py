from urllib.parse import quote_plus

class Config:
    SQLALCHEMY_DATABASE_URI= 'sqlite:///mydatabase.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False