from flask.wrappers import Request
from POFWebpage import app, db
from flask import render_template, redirect, url_for, flash, request
from POFWebpage.forms import RegistrationForm, LoginForm, MailingListForm
from POFWebpage.UserClass import User
import hashlib, os, binascii

@app.route('/', methods = ["GET", "POST"])
@app.route('/home', methods = ["GET", "POST"])
def home_page():
    checkDBWorking(db)
    #print(request.form.get('email'))
    if request.method == 'POST':
        if db.addToEmailList(request.form.get('email')):
            flash(f'You were added to the mailing list', 'success')
            return render_template('pof_home.html')
        else:
            flash(f'There was an issue adding you to the mailing list', 'danger')
            return render_template('pof_home.html')           
    return render_template('pof_home.html')

@app.route('/about')
def about_page():
    checkDBWorking(db)
    return render_template('pof_about.html')

@app.route('/contact')
def contact_page():
    checkDBWorking(db)
    return render_template('pof_contact.html')

@app.route('/login', methods = ["GET", "POST"])
def login_page():
    checkDBWorking(db)
    form = LoginForm()
    #if submitted data is valid with the form
    if form.validate_on_submit():

        #try:  
            #newUser = User(form.username.data, form.email.data, form.password.data)
            #check if username exists
            if db.checkForUser(form.username.data):
                #Get user from database
                checkUser = db.getUser(form.username.data)
                if User.jsonToUser(checkUser).checkPassWordsMatch(form.password.data):
                    flash(f'Successfully logged into user: {form.username.data}', 'success')
                    return redirect(url_for('about_page'))
                else:
                    flash(f'Password does not match', 'danger')
                    return render_template('pof_login.html', form = form)
            else:
                flash(f'Username does not exist', 'danger')
                return render_template('pof_login.html', form = form)
        #except:
        #    print("Error logging in. Please try again")
        #    return render_template('pof_login.html', form = form)
    return render_template('pof_login.html', title ='Login', form = form)


@app.route('/register', methods = ["GET", "POST"])
def registration_page():
    checkDBWorking(db)
    form = RegistrationForm()
    if form.validate_on_submit():
        try:  
            newUser = User(form.username.data, form.email.data, form.password.data)
            if db.addUser(newUser.userToJson()):
                flash(f'Account created for {form.email.data}', 'success')
                return redirect(url_for('about_page'))
            else:
                flash(f'Username {form.username.data} already exists', 'danger')
                return render_template('pof_registration.html', form = form)
        except:
            print("Error making user. Please try again")
            return render_template('pof_registration.html', form = form)
    return render_template('pof_registration.html', form = form)



###Helper Functions###

#Requires: POFDB class db
#Modifies: Flashed message to website
#Effects: When called and passed a db object, will check the database connection status. If the status is false,
#the an error will be flashed to the website
def checkDBWorking(DB):
    if DB.getConnectionStatus() == False:
        flash(f'Error: Unable to connect to database', 'danger')
    else:
        return