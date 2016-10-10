from flask.ext.script import Manager, Server
from app import app
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding()!= default_encoding:
	reload(sys)
	sys.setdefaultencoding(default_encoding)
manager=Manager(app)

manager.add_command("runserver",Server(
	use_debugger=True,
	use_reloader=True,
	host='0.0.0.0')
)
if __name__=="__main__":
	manager.run()

