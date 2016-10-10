from app import db

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	username = db.Column(db.String(255), nullable=True)
	userid = db.Column(db.String(255), nullable=True,index=True)
	passwd = db.Column(db.String(255), nullable=True)
	source = db.Column(db.String(255), nullable=True)

