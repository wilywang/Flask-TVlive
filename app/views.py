from flask.views import MethodView
from app.tvlist import tvdic
from app.tvurl import tvurl
from flask import Blueprint,request,render_template
acv=Blueprint('tv_v', __name__, template_folder='templates',static_folder='static')


class ListTV(MethodView):
	
	def get(self):
		return render_template('main.html',chanel="btv1",name=tvdic["btv1"],url=tvurl["btv1"])

	def post(self):
		return render_template('main.html',chanel="btv1",name=tvdic["btv1"],url=tvurl["btv1"])
class OneTV(MethodView):
	def get(self,slug):
		if slug.find("cctv")>=0:
			url='http://live.64ma.com/tv/tv.asp?pid=%s&user=simon&lm=1' % slug
		else:
			url=tvurl[slug]
		return render_template('index.html',name=tvdic[slug],chanel=slug,url=url) 
	def post(self,slug):
		if slug.find("cctv")>=0:
                        url='http://live.64ma.com/tv/tv.asp?pid=%s&user=simon&lm=1' % slug
                else:
                        url=tvurl[slug]
                return render_template('index.html',name=tvdic[slug],chanel=slug,url=url)

class Link(MethodView):
        def get(self):
                return render_template('link.html')
        def post(self):
                return render_template('link.html')

class IframeTV(MethodView):
        def get(self,slug):
                if slug == "hunan":
			return render_template('hunanws.html')                        
                elif slug == "jiangsu":
			return render_template('jiangsu.html')
		else:
                	return render_template('hunanws.html')
        def post(self,slug):
                if slug == "hunan":
                        return render_template('hunanws.html')
                elif slug == "jiangsu":
                        return render_template('jiangsu.html')
                else:
                	return render_template('hunanws.html')



#@acv.route('/ch/<slug>')
def hello_user(slug):
	return "Hello %s!" % slug
acv.add_url_rule('/',view_func=ListTV.as_view('mainpage'))
#acv.add_url_rule('/lst.html',view_func=ListAccount.as_view('list1'))
#acv.add_url_rule('/lst1.html',view_func=ListAccount.as_view('list2'))
acv.add_url_rule('/ch/<slug>.html/',view_func=OneTV.as_view('onetv'))
acv.add_url_rule('/about.html',view_func=Link.as_view('link'))
acv.add_url_rule('/app/<slug>.shtml/',view_func=IframeTV.as_view('iframetv'))
