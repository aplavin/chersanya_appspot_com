# -*- coding: utf-8 -*-

import webapp2
import os
import logging
from datetime import datetime, timedelta, date, time
import jinja2
from google.appengine.ext import db
import urllib
import base64
from operator import itemgetter, attrgetter
from collections import Counter, defaultdict

class O(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
		
class ApplicationModel(db.Model):
	name = db.StringProperty()
	version = db.StringProperty()
	date = db.DateTimeProperty()
	text_ru = db.TextProperty()
	text_en = db.TextProperty()
	file = db.BlobProperty()
	screenshots = db.ListProperty(db.Blob)
		
		
langs_list = [('ru', u'Русский'), ('en', u'English')]

jinja = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	line_statement_prefix = '#',
	line_comment_prefix = '##')

jinja.globals['uri_for'] = webapp2.uri_for
jinja.globals['langs'] = langs_list
jinja.globals['str'] = str