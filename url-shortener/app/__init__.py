from flask import Flask, request, redirect
from .short import short_url
from .models import db
from flask_migrate import Migrate


app = Flask(__name__)
# db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.sqlite3'
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(short_url)