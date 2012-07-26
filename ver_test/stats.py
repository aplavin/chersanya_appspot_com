# -*- coding: utf-8 -*-

from import_me import *
from google.appengine.api import backends, urlfetch, taskqueue

class CachedStats(db.Model):
	date = db.DateTimeProperty(auto_now = True)
	content = db.TextProperty(required = True)

class Stats(webapp2.RequestHandler):
	def get(self, force_gen = None):			
		item = CachedStats.all().get()
		if not item:
			item = O(date = datetime.now(), content = 'No stats')
		
		template_values = {
			'date': item.date,
			'content': item.content,
		}
		
		if force_gen or datetime.now() - item.date > timedelta(hours = 1):
			taskqueue.add(url='/stats/generate', target='stats-generator', method='GET')
		
		self.response.out.write(jinja.get_template('stats.html').render(template_values))