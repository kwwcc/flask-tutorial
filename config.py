import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'these-are-not-the-droids-you-are-looking-for'
    