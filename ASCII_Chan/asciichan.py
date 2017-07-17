import os
import webapp2
import jinja2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
								autoescape=True)

class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		return t.render(params)

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class Art(db.Model):
	title = db.StringProperty(required=True)
	art = db.TextProperty(required=True)
	created = db.DateTimeProperty(auto_now_add=True)

class MainPage(Handler):
	def render_front(self, title="", art="", error="", password=""):
		arts = db.GqlQuery("select * from Art order by created desc")



		self.render("front.html", title=title, art=art, error=error, arts=arts, password=password)

	def get(self):
		self.render_front()

	def post(self):
		title = self.request.get("title")
		art = self.request.get("art")
		password = self.request.get("password")

		if title and art and password == "akalight":
			a = Art(title=title, art=art)
			a.put()
			self.redirect("/")
		else:
			error = "Request not accepted"
			self.render_front(title,art, error)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)