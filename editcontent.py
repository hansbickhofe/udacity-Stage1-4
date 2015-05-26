#!/usr/bin/env python

from google.appengine.api import users
from ndbclasses import *
from google.appengine.ext import ndb
import webapp2
import jinja2
import logging
import os
import cgi
from webapp2_extras import json

#Constants for this Stage 
TITLE = 'Stage4'
SUBTITLE = '"Allow Comments on your Page"'
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'jinja2_templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR),autoescape = True)
DEFAULT_NOTES = 'Notes'

def note_key(note_name=DEFAULT_NOTES):
	"""Constructs a Datastore key for a Note entity.

	We use note_name as the key.
	"""
	return ndb.Key('Note', note_name)
	
# using Handler from Videolesson		
class Handler(webapp2.RequestHandler):
	def write(self, *a, **kw):
		self.response.out.write(*a,**kw)
	
	def render_str(self, template, **params):
		t = JINJA_ENVIRONMENT.get_template(template)
		return t.render(params)
	
	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))

class EditContentHandler(Handler):
	def get(self):
		self.redirect("/")		
		
	def post(self):
		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			user_mail = user.email()
			user_nickname = user.nickname()
			user_userid = user.user_id()

			if cgi.escape(self.request.get("edit")) == "1" and users.is_current_user_admin():
				note_to_edit = int(cgi.escape(self.request.get("note_id")))
				note = Article.get_single(note_to_edit)
				logging.info(str(note))
				self.render('contentform.html', pagetitle = TITLE, pagesubtitle = SUBTITLE, editnote = note, user = user_userid, loginurl = url, linktext = url_linktext)
			else:
				header = cgi.escape(self.request.get("header"))
				subheader = cgi.escape(self.request.get("subheader"))
				note = self.request.get("note")
				noteindex = int(cgi.escape(self.request.get("noteindex")))
				# Using Ancestor Queries, because of their strong consistensy
				note_name = DEFAULT_NOTES
				newarticle = Article(parent=note_key(note_name))
				newarticle.header = header
				newarticle.subheader = subheader
				newarticle.noteid = noteindex
				newarticle.note = note
				newarticle.put()
				self.redirect("/")							
		else:
			self.redirect("/")							
	
app = webapp2.WSGIApplication([
	('/editcontent', EditContentHandler),
], debug=True)		