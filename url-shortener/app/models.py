# from app import db
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Urls(db.Model):
	id = db.Column('id', db.Integer, primary_key = True)
	url = db.Column(db.String(100))
	shorten = db.Column(db.String(50))

	def __init__(self, url, shorten):
		self.url = url
		self.shorten = shorten