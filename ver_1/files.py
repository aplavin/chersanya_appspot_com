from import_me import *
import mimetypes
mimetypes.init()

class FileDownload(webapp2.RequestHandler):
	def get(self, file):
		referer = self.request.headers.get("Referer")
		if referer and self.request.host not in referer:
			self.response.out.write('Hotlinking is not allowed.<br/><a href="/">Main page</a>')
		else:
			(type, encoding) = mimetypes.guess_type(file)
			if not type:
				type = "application/octet-stream"
			self.response.headers["Content-Type"] = type
			self.response.headers["Content-Disposition"] = "attachment"
			with open('files/' + file, 'rb') as f:
				self.response.out.write(f.read())

app = webapp2.WSGIApplication([webapp2.Route('/files/<file>', handler=FileDownload, name='file_download')])