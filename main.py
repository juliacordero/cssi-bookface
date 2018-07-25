import webapp2
import jinja2
import os

from google.appengine.ext import ndb

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class Message(ndb.Model):
    content = ndb.StringProperty()
    name = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
    def get(self): #for a get request
        templateVars = {
            'messages' : messages,
        }
        template = env.get_template('templates/home.html')
        self.response.write(template.render(templateVars)) #the response


app = webapp2.WSGIApplication([
    ('/', MainPage), #this maps the root url to the Main Page Handler

], debug=True)
 
