
from import_me import *
from receivers import ErrorReport

class ViewErrorReport(webapp2.RequestHandler):
	def get(self):
		ers = list(ErrorReport.all())
			
		template_values = {
			'headers': ers[0].__dict__.keys(),
			'ers': [[value for key, value in er.__dict__.items()] for er in ers]
		}	
		
		self.response.out.write(jinja.get_template('view_error_reports.html').render(template_values))