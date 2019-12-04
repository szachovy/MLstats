#!/usr/bin/env python3

__author__ = 'WJ Maj'

from flask import Flask
from flask_testing import TestCase

class App(TestCase):
    '''
    Test reliability of web interface
    '''
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        return app
