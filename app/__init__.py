from flask import Flask

app=Flask(__name__)

def register_views(app):
	from app.views import acv
	app.register_blueprint(acv)

register_views(app)
