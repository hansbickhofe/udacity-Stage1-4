from google.appengine.ext import ndb

DEFAULT_NOTES = 'Notes'
DEFAULT_COMMENTS = 'Comments'

def note_key(note_name=DEFAULT_NOTES):
	"""Constructs a Datastore key for a Note entity.

	We use note_name as the key.
	"""
	return ndb.Key('Note', note_name)

def comment_key(comment_name=DEFAULT_COMMENTS):
	"""Constructs a Datastore key for a Comment entity.

	We use comment_name as the key.
	"""
	return ndb.Key('Comment', comment_name)
  
class Article(ndb.Model):
	""" ndb Model for an Article """
	note = ndb.TextProperty(indexed=False)
	header = ndb.StringProperty(indexed=True)
	subheader = ndb.StringProperty(indexed=False)
	
	@classmethod
	def get_all(self):
		# Using Ancestor Queries, because of their strong consistensy
		note_name = DEFAULT_NOTES
		all_notes = self.query(ancestor = note_key(note_name)).order(self.header).fetch()
		return all_notes
	
class Author(ndb.Model):
	"""ndb Model for an author."""
	userid = ndb.StringProperty(indexed=True)
	name = ndb.StringProperty(indexed=False)
	email = ndb.StringProperty(indexed=False)
	
class Comment(ndb.Model):
	"""ndb Model for the comment."""
	commentauthor = ndb.StructuredProperty(Author)
	commentednote = ndb.StructuredProperty(Article)
	commentext = ndb.StringProperty(indexed=True)
	commentdate = ndb.DateTimeProperty(auto_now_add=True)

	@classmethod
	def get_all_comments(self):
		all_comments = Comment.query().order(commentdate).fetch()
		return all_comments
	
class Vocabulary(ndb.Model):
	word = ndb.StringProperty(indexed=True)
	description = ndb.StringProperty(indexed=False)
	