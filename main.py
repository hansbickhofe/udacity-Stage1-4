#!/usr/bin/env python
# -*- coding: utf-8 -*-
from google.appengine.api import users
from google.appengine.ext import ndb
from ndbclasses import *
import webapp2
import jinja2
import logging
import os
import cgi
from webapp2_extras import json
import pprint

#Constants for this Stage 
TITLE = 'Stage4'
SUBTITLE = '"Allow Comments on your Page"'
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'jinja2_templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR),autoescape = True)

# using Handler from Videolesson	
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)
	
	def render_str(self, template, **params):
		t = JINJA_ENVIRONMENT.get_template(template)
		return t.render(params)
	
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


class MainHandler(Handler):
    def get(self):
		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			user_mail = user.email()
			logging.info("debug " + user_mail)
		else:
			user = 'Anonymous Poster'
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			user_mail = ""
		notes = Article.get_all()
			
		self.render('content.html', pageheader = 'Udacity ND Programing', lesson_notes = notes, pagetitle = TITLE, pagesubtitle = SUBTITLE, user=user_mail, loginurl = url, linktext = url_linktext)
		
app = webapp2.WSGIApplication([
	('/', MainHandler),
], debug=True)
