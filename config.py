import os
from dotenv import load_dotenv, dotenv_values

# load from .env
load_dotenv()


# Create a class of imported constants from .env file
class Config:
    MARXZI_DATABASE_URI = os.getenv('MARXZI_DATABASE_URI')
    FLASK_SECRET_KEY = os.getenv('FLASK_SECRET_KEY')
    MARXZI_EMAIL = os.getenv('MARXZI_EMAIL')
    SMTP_EMAIL_SERVER = os.getenv('SMTP_EMAIL_SERVER')
    SERVER_EHLO = os.getenv('SERVER_EHLO')
    APP_PASSWORD = os.getenv('APP_PASSWORD')
    HOST = os.getenv('HOST')
    PORT = os.getenv('PORT')