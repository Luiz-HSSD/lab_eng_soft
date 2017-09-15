"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
import FlaskWebProject2.views
import FlaskWebProject2.Controllers