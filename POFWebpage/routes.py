from POFWebpage import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('pof_home.html')

@app.route('/about')
def about_page():
    return render_template('pof_about.html')

@app.route('/contact')
def contact_page():
    return render_template('pof_contact.html')

@app.route('/login')
def login_page():
    return render_template('pof_login.html')