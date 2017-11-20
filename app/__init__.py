from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO1_DBNAME'] = 'flappy'
mongo = PyMongo(app, config_prefix='MONGO1')
from app import views
app.config.from_object('config')