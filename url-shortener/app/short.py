from flask import Blueprint, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
import re, random
import hashlib
# from app import app
from .models import Urls, db


short_url = Blueprint('short_url', __name__,)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.sqlite3'

rndlam = lambda str : random.choice(str) if random.choice('10') == 1 else random.choice(str).upper()

def generate_hash(url, length=6):
	sha256 = hashlib.sha256(url).hexdigest()
	rndStr = ''.join(rndlam(sha256) for x in range(length))
	return sha256, rndStr

@short_url.route('/url/short', methods = ['POST'])
def shorten_the_url():
	# data = request.get_json()
	# data = request.args
	data = request.json
	if not data or not data.get('long_url'):
		return {
		'Error' : "URL required"
		}
	url = data.get('long_url')
	try:
		rndStr = Urls.query.filter_by(url = url).first()
	except NoResultFound as e:
		rndStr = None
	
	if rndStr:
		return request.url_root + rndStr.shorten 
	
	shorten, rndStr = generate_hash(url.encode('utf-8'))
	obj = Urls(url, rndStr)
	db.session.add(obj)
	db.session.commit()
	return request.url_root + rndStr 

@short_url.route('/<slug>', methods=['GET'])
def redirect_url(slug):
	if not slug:
		return "Haha Working !!"
	try:
		long_url = Urls.query.filter_by(shorten = slug).first()
		if not long_url:
			# return "Haha Working !!"
			return render_template('invalid.html'), 404
		long_url = long_url.url
	except NoResultFound as e:
		pass
	else:
		return redirect(long_url)
