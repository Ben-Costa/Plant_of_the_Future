from POFWebpage import app, db
from flask import render_template, redirect, url_for, flash, redirect
from POFWebpage.forms import RegistrationForm, LoginForm
from POFWebpage.UserClass import User
import hashlib

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

@app.route('/login', methods = ["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "bc234cc@gmail.com" and form.password.data == "321BHC123":
            flash('Logged in as Admin', 'success')
            return redirect(url_for('about_page'))
        else:
            flash(f'User does not exist', 'danger')
    return render_template('pof_login.html', title ='Login', form = form)

@app.route('/register', methods = ["GET", "POST"])
def registration_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        
        print('hi')

        #convert password to sha256 hash
        hash_pass = hashlib.sha256()### this creates hash, not the hash password, will need to store both
        print(hash_pass.hexdigest())
        ###################need to test
        try:  
            newUser = User(form.username, form.email, hash_pass)
        except:
            print("Error making user. Please try again")

        flash(f'Account created for {form.email.data}', 'success')
        return redirect(url_for('about_page'))
    return render_template('pof_registration.html', form = form)