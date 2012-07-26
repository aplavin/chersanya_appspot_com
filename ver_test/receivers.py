# -*- coding: utf-8 -*-

from import_me import *

def force_utf8(string):
    if type(string) == str:
        return string
    return string.encode('utf-8')

def force_unicode(string):
    if type(string) == unicode:
        return string
    return string.decode('utf-8')

class DeviceEntry(db.Model):
	app_name = db.StringProperty(required = True)
	id = db.StringProperty(required = True)
	date = db.DateTimeProperty(auto_now_add = True)	
	
class SongEntry(db.Model):
	id = db.StringProperty(required = True)
	song = db.StringProperty(required = True)
	date = db.DateTimeProperty(auto_now_add = True)
	
class TidStatsEntry(db.Model):
	date = db.DateTimeProperty(auto_now_add = True)
	id = db.StringProperty(required = True)
	version = db.IntegerProperty(required = True)
	action = db.StringProperty(required = True)
	song = db.StringProperty(required = True)
	data = db.StringProperty(required = True)
	
class ErrorReport(db.Model):
	date = db.DateTimeProperty(auto_now_add = True)
	app_name  = db.StringProperty(required = True)
	
	exStackTrace  = db.TextProperty()
	exClass = db.StringProperty()
	exMessage = db.TextProperty()
	exDateTime = db.StringProperty()
	extraMessage = db.TextProperty()
	exThreadName = db.StringProperty()
	appVersionCode = db.IntegerProperty()
	appVersionName = db.StringProperty()
	appPackageName = db.StringProperty()
	devAvailableMemory = db.IntegerProperty()
	devTotalMemory = db.IntegerProperty()
	devModel = db.StringProperty()
	devSdk = db.IntegerProperty()
	devReleaseVersion= db.StringProperty()

class Receivers(webapp2.RequestHandler):
	def receive_device_id(self, app_name, id):
		entry = DeviceEntry(app_name=app_name, id = id)
		entry.put()		
		
	def receive_song(self, id, song):
		entry = SongEntry(id = id, song = force_unicode(song))
		entry.put()
		
	def receive_tiddownloader(self):
		entry = TidStatsEntry(
			id = self.request.get('id'),
			version = int(self.request.get('version')),
			action = self.request.get('action'),
			song = self.request.get('song'),
			data = self.request.get('data')
		)
		entry.put()
		
	def receive_error_report(self, app_name):
		report = ErrorReport(app_name=app_name)
		
		report.exStackTrace = self.request.get('exStackTrace')
		report.exClass = self.request.get('exClass')
		report.exMessage = self.request.get('exMessage')
		report.exDateTime = self.request.get('exDateTime')
		report.extraMessage = self.request.get('extraMessage')
		report.exThreadName = self.request.get('exThreadName')
		report.appVersionCode = int(self.request.get('appVersionCode'))
		report.appVersionName = self.request.get('appVersionName')
		report.appPackageName = self.request.get('appPackageName')
		report.devAvailableMemory = int(self.request.get('devAvailableMemory'))
		report.devTotalMemory = int(self.request.get('devTotalMemory'))
		report.devModel = self.request.get('devModel')
		report.devSdk = int(self.request.get('devSdk'))
		report.devReleaseVersion = self.request.get('devReleaseVersion')
		
		report.put()