
from import_me import *
import gviz_api
from receivers import ErrorReport, SongEntry
from google.appengine.api import logservice
from stats import CachedStats
		
		
def gen_tiddownload():
	template_values = {}
	reports = list(ErrorReport.all())
	
	# error reports chart
	vers = set(r.appVersionName for r in reports)
	reps_by_ver = {ver: [r for r in reports if r.appVersionName == ver] for ver in vers}
	
	data = [{'version': ver, 'reports': len(reps), 'unique': len(set(r.exStackTrace for r in reps))} for ver, reps in sorted(reps_by_ver.items())]
	description = {
		'version': ('string', 'Version'),
		'reports': ('number', 'Total'),
		'unique': ('number', 'Unique'),
	}
			
	data_table = gviz_api.DataTable(description)
	data_table.LoadData(data)
	template_values['error_reports_json'] = data_table.ToJSon(columns_order=('version', 'reports', 'unique'))
	
	# error reports statistics
	stats = []
	template_values['error_reports_stats'] = stats
	
	stats.append(('Total reports', len(reports)))
	stats.append(('Unique reports', len(set(r.exStackTrace for r in reports))))
	maxVerCode = max(reports, key=attrgetter('appVersionCode')).appVersionCode
	stats.append(('Last report (last version)', max((r for r in reports if r.appVersionCode != maxVerCode), key=attrgetter('date')).date + timedelta(hours = 4)))
	
	
	# songs chart
	songs = list(SongEntry.all())
	dates = set(s.date.date() for s in songs)
	data = [{
		'date': date,
		'total': len([s for s in songs if s.date.date() == date]),
		'unique': len(set(s.song for s in songs if s.date.date() == date)),
		'users': len(set(s.id for s in songs if s.date.date() == date)),
	} for date in dates]
	
	data_aggr = [{
		'date': date,
		'total': len([s for s in songs if s.date.date() <= date]),
		'unique': len(set(s.song for s in songs if s.date.date() <= date)),
		'users': len(set(s.id for s in songs if s.date.date() <= date)),
	} for date in dates]
	
	description = {
		'date': ('date', 'Date'),
		'total': ('number', 'Total'),
		'unique': ('number', 'Unique'),
		'users': ('number', 'Users'),
	}
	
	data_table = gviz_api.DataTable(description)
	data_table.LoadData(data)
	template_values['songs_json'] = data_table.ToJSon(columns_order=('date', 'total', 'unique', 'users'), order_by='date')
	
	data_table = gviz_api.DataTable(description)
	data_table.LoadData(data_aggr)
	template_values['songs_aggr_json'] = data_table.ToJSon(columns_order=('date', 'total', 'unique', 'users'), order_by='date')
	
	# songs statistics
	stats = []
	template_values['songs_stats'] = stats
	
	stats.append(('Total searches', len(songs)))
	stats.append(('Unique searches', len(set(s.song for s in songs))))
	stats.append(('Unique users', len(set(s.id for s in songs))))
	
	stats.append(('', ''))
	stats.append(('Most popular song:', ''))
	
	max_pop = max(((s.song.replace('+', ' '), len(set(ss.id for ss in songs if ss.song == s.song))) for s in songs), key = itemgetter(1))
	stats.append(max_pop)
		
	# logs
	request_logs = sorted(list(logservice.fetch()) + list(logservice.fetch(version_ids = ['1'])), key = attrgetter('start_time'))
	dates = set(datetime.fromtimestamp(r.start_time).date() for r in request_logs)		
	data = [{
		'date': date,
		'requests': len([r for r in request_logs if datetime.fromtimestamp(r.start_time).date() == date]),
		'ips': len(set(r.ip for r in request_logs if datetime.fromtimestamp(r.start_time).date() == date)),
	} for date in dates]
	
	description = {
		'date': ('date', 'Date'),
		'requests': ('number', 'Requests'),
		'ips': ('number', 'IPs'),
	}
			
	data_table = gviz_api.DataTable(description)
	data_table.LoadData(data)
	template_values['logs_json'] = data_table.ToJSon(columns_order=('date', 'requests', 'ips'), order_by='date')
	
	template_values['logs'] = [
		('Count', len(request_logs)),
		('Cost', sum(r.cost for r in request_logs)),
	]
	
	for item in CachedStats.all():
		item.delete()
			
	res = CachedStats(content = jinja.get_template('tiddownload_stats.html').render(template_values))
	res.put()
	
	
class Generator(webapp2.RequestHandler):
	def get(self):
		logging.info('GenStarted')
		#gen_tiddownload()
		logging.info('GenStoppped')
		logservice.flush()