
from import_me import *
from receive_song import SongEntry
from collections import defaultdict
import urllib2


class ViewSongs(webapp2.RequestHandler):
    def get(self):
		dct = defaultdict(list)
		
		for se in SongEntry.all():
			dct[se.id].append((se.date + timedelta(hours = 4), urllib2.unquote(se.song.replace('+', ' '))))
			
		for id in dct:
			dct[id].sort()
			
		template_values = {'ids': sorted(dct.items())}
			
		self.response.out.write(jinja.get_template('view_songs.html').render(template_values))
		

app = webapp2.WSGIApplication([webapp2.Route('/view_songs', handler=ViewSongs, name='view_songs'),])