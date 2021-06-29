from flask import Flask

app = Flask(__name__, static_folder="../POFWebpage/static")

from POFWebpage import routes