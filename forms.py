from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')

class AddWishForm(FlaskForm):
    item = StringField('Item', validators=[DataRequired()])
    description = TextField('Description')
