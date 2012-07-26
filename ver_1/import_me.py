
import webapp2
from webapp2_extras import routes
import os
import logging
from datetime import datetime, timedelta
import jinja2
from google.appengine.ext import db

class O(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
		

default_lang = open('langs/default').readline()
langs_list = [(name, open(os.path.join('langs', name)).readline().decode('utf-8')) for name in os.listdir('langs') if os.path.isfile(os.path.join('langs', name)) and not name == 'default']

jinja = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	line_statement_prefix = '#',
	line_comment_prefix = '##')

def relative_datetime(value, lang):
	s = (datetime.utcnow() - value).total_seconds()
	s += 4 * 3600
	if s < 5 * 60:
		return 'just now'
	elif s < 3600:
		return 'an hour ago'
	elif s < 24 * 3600:
		return 'today'
	else:
		return value.strftime('%d.%m.%Y')
	

jinja.filters['time_rel'] = relative_datetime