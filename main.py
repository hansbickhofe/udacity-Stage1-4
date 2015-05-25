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
from collections import namedtuple
import pprint

#Constants for this Stage 
TITLE = 'Stage4'
SUBTITLE = '"Allow Comments on your Page"'
TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'jinja2_templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR),autoescape = True)
DEFAULT_COMMENTS = 'Comments'
ARTICLE = namedtuple('Article', ['header','subheader','note','noteid','comments'])
COMMENT = namedtuple('Comment', ['commentednote','commentauthor','commenttext'])

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
		notes_list = []
		user = users.get_current_user()
		if user:
			url = users.create_logout_url(self.request.uri)
			url_linktext = 'Logout'
			user_mail = user.email()
			user_nickname = user.nickname()
			user_userid = user.user_id()
		else:
			user = 'Anonymous Poster'
			url = users.create_login_url(self.request.uri)
			url_linktext = 'Login'
			user_mail = ""
			
		
		notes = Article.get_all()
		
		for note in notes:			
			comments = Comment.get_all(note.noteid)
			comment_list = []
			for comment in comments:
				comment_list += [COMMENT(note.noteid,comment.commentauthor.name, comment.commenttext)]
			notes_list += [ARTICLE(note.header, note.subheader, note.note, note.noteid, comment_list)]

		logging.info("Note: " + str(notes_list))
		self.render('content.html', pageheader = 'Udacity ND Programing', lesson_notes = notes_list, pagetitle = TITLE, pagesubtitle = SUBTITLE, user=user_mail, loginurl = url, linktext = url_linktext )
	
	def post(self):
		comment_name = (DEFAULT_COMMENTS)
		user = users.get_current_user()
		if user:
			note_id = int(cgi.escape(self.request.get("note_id")))
			comment = cgi.escape(self.request.get("comment"))
			# Using Ancestor Queries, because of their strong consistensy
			newcomment = Comment(parent=comment_key(comment_name))
			newcomment.commentednote = note_id
			newcomment.commenttext = comment
			newcomment.commentauthor = Author(
				userid = user.user_id(),
				name = user.nickname(),
				email = user.email(),
				)
			newcomment.put()
			self.redirect("/")
						
		
app = webapp2.WSGIApplication([
	('/', MainHandler),
], debug=True)
