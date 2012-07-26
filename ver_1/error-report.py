# -*- coding: utf-8 -*-

from import_me import *

class ErrorReport(db.Model):
	date = db.DateTimeProperty(auto_now_add=True)
	app_name  = db.StringProperty(required = True)
	
	exStackTrace  = db.TextProperty()
	exClass = db.StringProperty()
	exMessage = db.TextProperty()
	exDateTime = db.StringProperty()
	extraMessage = db.TextProperty()
	exThreadName = db.StringProperty()
	appVersionCode = db.StringProperty()
	appVersionName = db.StringProperty()
	appPackageName = db.StringProperty()
	devAvailableMemory = db.StringProperty()
	devTotalMemory = db.StringProperty()
	devModel = db.StringProperty()
	devSdk = db.StringProperty()
	devReleaseVersion= db.StringProperty()	

class IdReceiver(webapp2.RequestHandler):
    def post(self, app_name):
		report = ErrorReport(app_name=app_name)
		
		report.exStackTrace = self.request.get('exStackTrace')
		report.exClass = self.request.get('exClass')
		report.exMessage = self.request.get('exMessage')
		report.exDateTime = self.request.get('exDateTime')
		report.extraMessage = self.request.get('extraMessage')
		report.exThreadName = self.request.get('exThreadName')
		report.appVersionCode = self.request.get('appVersionCode')
		report.appVersionName = self.request.get('appVersionName')
		report.appPackageName = self.request.get('appPackageName')
		report.devAvailableMemory = self.request.get('devAvailableMemory')
		report.devTotalMemory = self.request.get('devTotalMemory')
		report.devModel = self.request.get('devModel')
		report.devSdk = self.request.get('devSdk')
		report.devReleaseVersion = self.request.get('devReleaseVersion')
		
		report.put()
		

app = webapp2.WSGIApplication([webapp2.Route('/error-report/<app_name>', handler=IdReceiver, name='id_receiver'),])