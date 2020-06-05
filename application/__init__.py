from flask import Flask
from os import getenv
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=getenv('FLASKPROJECTDBURI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY']=getenv('SECRETKEY')
db = SQLAlchemy(app)

from application import routes
