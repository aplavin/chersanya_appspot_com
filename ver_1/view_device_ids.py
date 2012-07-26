
from import_me import *
from receive_device_id import DeviceEntry
from collections import defaultdict
from google.appengine.api import users


class ViewIds(webapp2.RequestHandler):
    def get(self):
		dct = defaultdict(list)
		for de in DeviceEntry.all():
			dct[de.id].append(de.date + timedelta(hours = 4))
			
		for id in dct:
			dct[id].sort()
			
		template_values = {'ids': sorted(dct.items())}
			
		self.response.out.write(jinja.get_template('view_device_ids.html').render(template_values))
		

app = webapp2.WSGIApplication([webapp2.Route('/view_device_ids', handler=ViewIds, name='view_ids'),])