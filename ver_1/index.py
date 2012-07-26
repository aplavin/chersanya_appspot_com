# -*- coding: utf-8 -*-

from import_me import *

class MainPage(webapp2.RequestHandler):
    def get(self, lang = None):
		if not lang:			
			lang = default_lang
			
		app_descs_dir = 'langs/apps'
		apps_list = []
		for file in (open(os.path.join(app_descs_dir, fname)) for fname in os.listdir(app_descs_dir) if fname.endswith('.' + lang)):
			lines = [line.decode('utf-8') for line in file.read().splitlines()]
			app = O()
			app.name = lines[0]
			app.page = lines[1]
			app.date = datetime.strptime(lines[2], '%d.%m.%Y %H:%M')
			app.ver = lines[3]
			app.apk = lines[4]
			app.imgs = lines[5].split()
			app.text = lines[6]
			
			apps_list.append(app)
		
		template_values = {
			'lang': lang,
			'langs': langs_list,
			'apps': apps_list
		}
		
		self.response.out.write(jinja.get_template('index.html').render(template_values))
		
class AppPage(webapp2.RequestHandler):
	def get(self, page, lang = None):
		if not lang:			
			lang = default_lang
			
		app_descs_dir = 'langs/apps'
		if os.path.isfile(os.path.join(app_descs_dir, page + '.' + lang)):
			file = open(os.path.join(app_descs_dir, page + '.' + lang))
			lines = [line.decode('utf-8') for line in file.read().splitlines()]
			app = O()
			app.name = lines[0]
			app.page = lines[1]
			app.date = datetime.strptime(lines[2], '%d.%m.%Y %H:%M')
			app.ver = lines[3]
			app.apk = lines[4]
			app.imgs = lines[5].split()
			app.text = '<br/>'.join(lines[6:])
			
		template_values = {
			'lang': lang,
			'langs': langs_list,
			'app': app
		}
		
		self.response.out.write(jinja.get_template('app.html').render(template_values))
			
		

app = webapp2.WSGIApplication([
	webapp2.Route('/', handler=MainPage, name='mainpage'),
	webapp2.Route('/<lang:\w{2}>', handler=MainPage, name='mainpage'),
	webapp2.Route('/apps/<page:\w+>.<lang:\w{2}>', handler=AppPage, name='mainpage'),
	webapp2.Route('/apps/<page:\w+>', handler=AppPage, name='mainpage'),
])