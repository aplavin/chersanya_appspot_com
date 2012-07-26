from import_me import *

class AppList(webapp2.RequestHandler):
    def get(self):
		apps = []
		for am in ApplicationModel.all():
			apps.append(O(name = am.name))
		
		template_values = {
			'apps': apps
		}
		
		self.response.out.write(jinja.get_template('admin_applist.html').render(template_values))
	
		
class App(webapp2.RequestHandler):
	def get(self, app_name):
		if app_name == 'NEW':
			template_values = {}
		else:
			q = ApplicationModel.all()
			q.filter("name =", app_name.decode('utf-8'))
			am = q.get()

			template_values = {
				'name': am.name,
				'version': am.version,
				'date': am.date,
				'text_en': am.text_en,
				'text_ru': am.text_ru,
				'scs_cnt': len(am.screenshots),
			}
		
		self.response.out.write(jinja.get_template('admin_app.html').render(template_values))
		
	def post(self, app_name):
		q = ApplicationModel.all()
		q.filter("name =", app_name.decode('utf-8'))
		am = q.get()
		if not am:
			am = ApplicationModel()
			
		am.date = datetime.now()
			
		am.name = self.request.get('name')
		am.version = self.request.get('version')
		am.text_en = self.request.get('text_en')
		am.text_ru = self.request.get('text_ru')
		try:
			am.file = db.Blob(self.request.POST.get('file').file.read())
		except AttributeError:
			pass
			
		scs = []
		for i in range(10):
			try:
				scs.append(db.Blob(self.request.POST.get('sc' + str(i)).file.read()))
			except AttributeError:
				pass
		if len(scs) > 0:
			am.screenshots = scs		
		
		am.put()
	
		self.redirect(webapp2.uri_for('admin_app_list'))