from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging

#Creates app object of type flask
app = Flask(__name__)
app.config.from_object('config')
# #Creates db object
# db = SQLAlchemy(app)
# #Creates login manager object
# login = LoginManager(app)
# #Creates a migrate instance
# migrate = Migrate(app, db)
# app.static_folder ='static'
# #The basic config for logging, format etc.
logging.basicConfig(filename='log.log', filemode='w', format='%(asctime)s | %(levelname)s:%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

from app import views, models
