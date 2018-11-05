from flask import Flask, redner_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)



def index():
    return '<p>hello</p>'


if __name__ == '__main__':
    app.run(debug=True)
