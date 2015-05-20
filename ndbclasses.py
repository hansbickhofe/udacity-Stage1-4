from google.appengine.ext import ndb
import logging


class Tags(ndb.Model):
	tagkey = ndb.KeyProperty(kind="Tag")
	tagstring = ndb.StringProperty(indexed=True)

class Article(ndb.Model):
	articlekey = ndb.KeyProperty(kind="Article")
	articletext = ndb.TextProperty(indexed=False)
	articletags = ndb.StringProperty(repeated=True)
	articlenumber = ndb.StringProperty(indexed=False)
	lessonheader = ndb.StringProperty(indexed=False)
	lessonsubheader = ndb.StringProperty(indexed=False)
	stagetitle = ndb.StringProperty(indexed=True)
	stagesubtitle = ndb.StringProperty(indexed=True)

	@classmethod
	def get_stage_lessons(self,stage):
		all_stage_lessons = Article.query(Article.stagetitle == stage).fetch()
		return all_stage_lessons
		
	@classmethod
	def get_all_lessons(self):
		all_lessons = Article.query().order(Article.lessonheader).fetch()
		return all_lessons
	

class Stage(ndb.Model):
	stagekey = ndb.KeyProperty(kind="Stage")
	stagetitle = ndb.StringProperty(indexed=True)
	stagesubtitle = ndb.StringProperty(indexed=True)
	
	@classmethod
	def get_all_stages(self):
		all_stages = Stage.query().order(Stage.stagetitle).fetch()
		return all_stages
	

class Comments(ndb.Model):
	commentkey = ndb.KeyProperty(kind="Comment")
	commenttext = ndb.TextProperty(indexed=False)
	
class Vocabulary(ndb.Model):
	word = ndb.StringProperty(indexed=True)
	description = ndb.StringProperty(indexed=False)
	