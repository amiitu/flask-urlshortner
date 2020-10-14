from flask import Flask, request, redirect
from .short import short_url
from .models import db
from flask_migrate import Migrate
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))
app = Flask(__name__)

if app.config["ENV"] == 'development':
	app.config.from_object("app.config.DevConfig")
elif app.config["ENV"] == 'production':
	app.config.from_object("app.config.ProdConfig")

db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(short_url)