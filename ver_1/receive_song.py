# -*- coding: utf-8 -*-

from import_me import *

def force_utf8(string):
    if type(string) == str:
        return string
    return string.encode('utf-8')

def force_unicode(string):
    if type(string) == unicode:
        return string
    return string.decode('utf-8')



class SongEntry(db.Model):
	id = db.StringProperty(required = True)
	song = db.StringProperty(required = True)
	date = db.DateTimeProperty(auto_now_add=True)

class SongReceiver(webapp2.RequestHandler):
    def get(self, id, song):
		entry = SongEntry(id = id, song = force_unicode(song))
		entry.put()
		

app = webapp2.WSGIApplication([webapp2.Route('/receive_song/<id>/<song>', handler=SongReceiver, name='song_receiver'),])