import re
import cgi
import webapp2

USER_RE = re.compile(r"[a-zA-Z0-9_-]{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")
PASS_RE = re.compile(r"^.{3,20}$")

def valid_username(s):
	return USER_RE.match(s)

def valid_email(s):
	return EMAIL_RE.match(s)

def valid_password(s):
	return PASS_RE.match(s)

form="""<form>
	<label>Username</label>
	<input name='username' type='text' align="right" value="%(username)s>
	<div style="color: red">%(name_error)s</div>
	<br>
	<label>Password</label>
	<input type="Password" name="password">
	<div style="color: red">%(pass_error)s</div>
	<br>
	<label>Verify Password</label>
	<input type="Password" name="verify">
	<div style="color:red">%(verify_error)s</verify>
	<br>
	<label>Email (optional)</label>
	<input type="text" name="email" value="%(email)s">
	<div style="color:red">%(email_error)s</div>
	<br>
	<input type="submit" value="Submit">
</form> """

class Main(webapp2.RequestHandler):
	def write_form(self,username='',email='',name_error='',pass_error='',verify_error='',email_error=''):
		return form % {"username": username,
						"email": email,
						"name_error": name_error,
						"pass_error": pass_error,
						"verify_error": verify_error,
						"email_error": email_error}

	def send_form(self, form):
		self.response.out.write(form)

	def get(self):
		self.write_form()

	def post(self):
		get_username = self.request.get('username')
		get_email = self.request.get('email')
		get_password = self.request.get('password')
		get_verifypassword = self.request.get('verify')

		username = valid_username(get_username)
		password = valid_password(get_password)
		verify_password = valid_password(get_verifypassword)
		email = valid_email(get_email)

		mapping={'username': username,
				'email': email,
				'verify': verify_password,
				'password': password}
		
application = webapp2.WSGIApplication([('/', Main),],debug = True)
