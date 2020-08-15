from flask import Flask

app = Flask(__name__)
FLASK_DEBUG=1

from app import routes