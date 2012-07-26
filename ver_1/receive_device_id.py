# -*- coding: utf-8 -*-

from import_me import *

class DeviceEntry(db.Model):
	app_name = db.StringProperty(required = True)
	id = db.StringProperty(required = True)
	date = db.DateTimeProperty(auto_now_add=True)

class IdReceiver(webapp2.RequestHandler):
    def get(self, app_name, id):
		entry = DeviceEntry(app_name=app_name, id = id)
		entry.put()
		

app = webapp2.WSGIApplication([webapp2.Route('/receive_device_id/<app_name>/<id>', handler=IdReceiver, name='id_receiver'),])