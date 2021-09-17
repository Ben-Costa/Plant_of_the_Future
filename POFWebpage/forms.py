from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField('username', validators= [DataRequired(), Length(min= 2, max=20)])
    email = StringField('email', validators= [DataRequired(), Email()])
    password = PasswordField('password', validators= [DataRequired()])
    confirm_password = PasswordField('password', validators= [DataRequired(), EqualTo('password')])
    submit = SubmitField('sign_up')

class LoginForm(FlaskForm):

    email = StringField('email', validators= [DataRequired(), Email()])
    password = PasswordField('password', validators= [DataRequired()])
    #remember = BooleanField('remeber_me')
    submit = SubmitField('login')