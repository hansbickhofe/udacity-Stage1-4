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

class AddContentHandler(Handler):
	def get(self):
		getall_stagetitles = Stage.get_all_stages()
		titles = []		
		subtitles = []		
		
		for stage in getall_stagetitles:
			titles.append(stage.stagetitle)	
			subtitles.append(stage.stagesubtitle)
						
		self.render('addcontentform.html', stagetitles = titles, stagesubtitles = subtitles)
		
	def post(self):
		getall_stagetitles = Stage.get_all_stages()
		titles = []		
		subtitles = []		
		for stage in getall_stagetitles:
			titles.append(stage.stagetitle)	
			subtitles.append(stage.stagesubtitle)
			lessons = ("")

		if cgi.escape(self.request.get("type")) == "stage":
			stagetitle = cgi.escape(self.request.get("stageno"))
			stagesubtitle = cgi.escape(self.request.get("stagesubtitle"))
			logging.info(self.request.get("stageno"))
			newstage = Stage()
			newstage.stagetitle = stageno
			newstage.stagesubtitle = stagesubtitle
			newstage.put()
		else: 
			stageno = cgi.escape(self.request.get("stageno"))
			stagesubtitle = cgi.escape(self.request.get("stagesubtitle"))
			lessonheader = cgi.escape(self.request.get("lessonheader"))
			lessonsubheader = cgi.escape(self.request.get("lessonsubheader"))
			articlenumber = cgi.escape(self.request.get("articlenumber"))
			lessontext = cgi.escape(self.request.get("lessontext"))
			lessontags = [cgi.escape(self.request.get("lessontags"))]
			logging.info(self.request.get("type"))
			lessons = ("")
			newarticle = Article()
			newarticle.lessonheader = lessonheader
			newarticle.lessonsubheader = lessonsubheader
			newarticle.articletext = lessontext
			newarticle.articletags = lessontags
			newarticle.stagetitle = stageno
			newarticle.articlenumber = articlenumber
			newarticle.stagesubtitle = stagesubtitle
			newarticle.put()
					
		self.render('addcontentform.html', stagetitles = titles, stagesubtitles = subtitles, lessonheaders = lessons, saved = "Saved!")
		
	
app = webapp2.WSGIApplication([
	('/addcontent', AddContentHandler),
], debug=True)		