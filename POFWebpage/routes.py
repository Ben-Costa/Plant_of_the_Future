from POFWebpage import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('base.html')

