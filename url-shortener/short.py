from flask import Flask, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.exc import NoResultFound
import re, random
import hashlib

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@127.0.0.1:3306/shorturl'
db = SQLAlchemy(app)

class Urls(db.Model):
	id = db.Column('id', db.Integer, primary_key = True)
	url = db.Column(db.String(100))
	shorten = db.Column(db.String(50))

	def __init__(self, url, shorten):
		self.url = url
		self.shorten = shorten
db.create_all()

rndlam = lambda str : random.choice(str) if random.choice('10') == 1 else random.choice(str).upper()

def generate_hash(url, length=6):
	sha256 = hashlib.sha256(url).hexdigest()
	rndStr = ''.join(rndlam(sha256) for x in range(length))
	return sha256, rndStr

@app.route('/url/short', methods = ['POST'])
def shorten_the_url():
	# data = request.get_json()
	data = request.args
	data = request.json
	if not data.get('long_url'):
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

@app.route('/<slug>', methods=['GET'])
def redirect_url(slug):
	if not slug:
		return "Haha Working !!"
	try:
		long_url = Urls.query.filter_by(shorten = slug).first()
		if not long_url:
			return "Haha Working !!"
		long_url = long_url.url
	except NoResultFound as e:
		pass
	else:
		return redirect(long_url)

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True, port=8001)
