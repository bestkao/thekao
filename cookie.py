from handler import *
import hmac

SECRET = "iamsosecret"

def hash_str(s):
	return hmac.new(SECRET, s).hexdigest()

def make_secure_val(s):
	return "%s|%s" % (s, hash_str(s))

def check_secure_val(h):
	val = h.split("|")[0]
	if h == make_secure_val(val):
		return val

class Cookie(Handler):
	def get(self):
		self.response.headers["Content-Type"] = "text/plain"
		visits = 0
		visit_cookie_str = self.request.cookies.get("visits")
		if visit_cookie_str:
			cookie_val = check_secure_val(visit_cookie_str)
			if cookie_val:
				visits = int(cookie_val)

		visits += 1
		
		new_cookie_val = make_secure_val(str(visits))

		self.response.headers.add_header("Set-Cookie", "visits=%s" % new_cookie_val)

		if visits > 10000:
			self.write("You are the best ever!")
		else:
			self.write("You've been here %s times!" % visits)