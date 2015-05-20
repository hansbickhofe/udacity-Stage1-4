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
import pprint

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), 'jinja2_templates')
JINJA_ENVIRONMENT = jinja2.Environment(loader = jinja2.FileSystemLoader(TEMPLATES_DIR),autoescape = True)
	
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

		getall_stagetitles = Stage.get_all_stages()
		titles = []		
		subtitles = []
		headers = []
		subheaders = [] 
		textcontent = []
		
		
		for stage in getall_stagetitles:
			titles.append(stage.stagetitle)	
			subtitles.append(stage.stagesubtitle)
			all_lessons = Article.get_stage_lessons(stage.stagetitle)
			
			for article in all_lessons:
				if article.stagetitle == stage.stagetitle:
					headers.append(article.lessonheader)
					subheaders.append(article.lessonsubheader)
					textcontent.append(article.articletext)
				
				
		self.render('stage.html', stagetitles = titles, stagesubtitles = subtitles, lesson_headers = headers, lesson_subheaders = subheaders, textcontent = textcontent)

app = webapp2.WSGIApplication([
	('/', MainHandler),
], debug=True)
