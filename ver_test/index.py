# -*- coding: utf-8 -*-

from import_me import *

class AppListPage(webapp2.RequestHandler):
    def get(self, lang):
		apps = []
		for am in ApplicationModel.all():
			apps.append(O(name = am.name, version = am.version, date = am.date, text = getattr(am, 'text_%s' % lang).split('\n')[0]))
			
		template_values = {
			'lang': lang,
			'apps': apps
		}
		
		self.response.out.write(jinja.get_template('index.html').render(template_values))
		
class AppPage(webapp2.RequestHandler):
	def get(self, app_name, lang):
		q = ApplicationModel.all()
		q.filter("name =", app_name.decode('utf-8'))
		am = q.get()
			
		template_values = {
			'lang': lang,
			'name': am.name,
			'version': am.version,
			'date': am.date,
			'scs_cnt': len(am.screenshots),
			'text': getattr(am, 'text_%s' % lang),
		}
		
		self.response.out.write(jinja.get_template('app_page.html').render(template_values))