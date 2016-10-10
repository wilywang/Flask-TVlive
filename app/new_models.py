from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/socdb?unix_socket=/tmp/mysql.sock'
db = SQLAlchemy(app)

class Account(db.Model):
	id = db.Column(db.Integer, primary_key=True,autoincrement=True)
	username = db.Column(db.String(255), nullable=True)
	userid = db.Column(db.String(255), nullable=True,index=True)
	passwd = db.Column(db.String(255), nullable=True)
	source = db.Column(db.String(255), nullable=True)

if __name__ == "__main__":
        db.create_all()


