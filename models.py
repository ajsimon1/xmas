from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    first_name = db.Column(String(25, nullable=False))
    last_name = db.Column(String(55), nullable=False)
    email = db.Column(String(120), unique=True, nullable=False)

class Wish(db.Model):
    wish_id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(55), nullable=False)
    description = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
