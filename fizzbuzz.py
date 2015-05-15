#!/usr/bin/env python

import os
import webapp2
import jinja2
import logging

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'jinja2_templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR))
	
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)
	
	def render_str(self, template, **params):
		t = JINJA_ENVIRONMENT.get_template(template)
		return t.render(params)
	
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class FizzBuzzHandler(Handler):	
	def get(self):
		n = self.request.get('n',0)
		n = n and int(n)
		self.render('fizzbuzz.html', fizzbuzz_title = "Fizz Buzz", n = n)


	

app = webapp2.WSGIApplication([
    ('/fizzbuzz', FizzBuzzHandler),
], debug=True)

