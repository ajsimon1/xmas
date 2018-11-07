from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from forms import LoginForm, RegisterForm


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

@app.route('/', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    return render_template('login.html', user='Adam', form=form)

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
