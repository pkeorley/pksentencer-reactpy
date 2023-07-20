from flask import Flask
from whitenoise import WhiteNoise

from modules.database import Database
from modules.parser import LetterParser


class FlaskApplication(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(__name__, *args, **kwargs)
        self.wsgi_app = WhiteNoise(self.wsgi_app, root="static/", prefix="assets/")
        self.database = Database()
        self.parser = LetterParser()
