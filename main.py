import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        self.response.write('Hello, World!') #the response

class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        welcome_template = env.get_template('templates/welcome.html')
        self.response.write(welcome_template.render())

class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        goodbye_template = env.get_template('templates/goodbye.html')
        self.response.write(goodbye_template.render())

app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler
    ('/welcome', WelcomeHandler),
    ('/goodbye', GoodbyeHandler)
], debug=True)
 
