from flask import Flask
from pymongo import MongoClient, mongo_client

app = Flask(__name__, static_folder="../POFWebpage/static")

app.config['SECRET_KEY'] = '123456789'

from POFWebpage import routes

#sudo mongod --dbpath ~/data/db - to run mongodb#

#thoughts- use https://pymongo.readthedocs.io/en/stable/tutorial.html to see if can connect to mongo alone
#next use https://stackabuse.com/integrating-mongodb-with-flask-using-flask-pymongo/ as it connects pymongo with flask 
