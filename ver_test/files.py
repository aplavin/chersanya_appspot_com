from import_me import *

class File(webapp2.RequestHandler):
	def get(self, app_name, img_num = None):
		referer = self.request.headers.get('Referer')
		
		if referer and self.request.host not in referer:
			self.response.out.write('Hotlinking is not allowed.<br/><a href="/">Main page</a>')
		else:	
			q = ApplicationModel.all()
			q.filter('name =', app_name.decode('utf-8'))
			am = q.get()
		
			if img_num:
				self.response.headers['Content-Type'] = 'image/png'
				content = am.screenshots[int(img_num)]
			else:
				self.response.headers['Content-Type'] = 'application/vnd.android.package-archive'
				self.response.headers['Content-Disposition'] = 'attachment; filename="%s.apk"' % app_name
				content = am.file
			
			self.response.out.write(content)