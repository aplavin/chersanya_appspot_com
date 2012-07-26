from webapp2 import WSGIApplication, Route
from webapp2_extras.routes import RedirectRoute

app = WSGIApplication([
	RedirectRoute('/', 								redirect_to_name = 'app_list_page', defaults = {'lang': 'ru'}),
	RedirectRoute('/<lang:\w{2}>', 					redirect_to_name = 'app_list_page'),
	
	RedirectRoute('/apps/tiddownload',				redirect_to_name = 'app_page', defaults = {'app_name': 'TrackID Download', 'lang': 'ru'}),
	RedirectRoute('/apps/tiddownload.<lang:\w{2}>',	redirect_to_name = 'app_page', defaults = {'app_name': 'TrackID Download'}),
	
	RedirectRoute('/apps/silentdroid',				redirect_to_name = 'app_page', defaults = {'app_name': 'SilentDroid', 'lang': 'ru'}),
	RedirectRoute('/apps/silentdroid.<lang:\w{2}>',	redirect_to_name = 'app_page', defaults = {'app_name': 'SilentDroid'}),

	RedirectRoute('/apps/',						redirect_to_name = 'app_list_page',						name = 'app_list_page', strict_slash = True, defaults = {'lang': 'ru'}),
	RedirectRoute('/<lang:\w{2}>/apps/',		handler = 'index.AppListPage', 							name = 'app_list_page', strict_slash = True),
	
	Route('/apps/<app_name>', 					handler = 'index.AppPage', 								name = 'app_page', defaults = {'lang': 'ru'}),
	Route('/<lang:\w{2}>/apps/<app_name>', 		handler = 'index.AppPage', 								name = 'app_page'),
	
	Route('/apks/<app_name>',	 				handler = 'files.File', 								name = 'apk'),
	Route('/imgs/<app_name>/<img_num>',			handler = 'files.File', 								name = 'img'),
	
	Route('/receive_device_id/<app_name>/<id>',	handler = 'receivers.Receivers:receive_device_id',		name = 'receive_device_id'),
	Route('/receive_song/<id>/<song>',			handler = 'receivers.Receivers:receive_song',			name = 'receive_song'),
	Route('/receive_trackiddownloader',			handler = 'receivers.Receivers:receive_tiddownloader',	name = 'receive_tiddownloader'),
	Route('/error-report/<app_name>',			handler = 'receivers.Receivers:receive_error_report',	name = 'receive_error_report'),
	
	Route('/view/error-reports',				handler = 'viewers.ViewErrorReport',					name = 'view_error_report'),
		
	Route('/admin/apps/', 						handler = 'admin.AppList', 								name = 'admin_app_list'),
	Route('/admin/apps/<app_name>', 			handler = 'admin.App', 									name = 'admin_app'),
	
	Route('/stats',								handler = 'stats.Stats',								name = 'stats'),
	Route('/stats/generate',					handler = 'stats_generator.Generator',					name = 'stats_generate'),
	Route('/stats/<force_gen>',					handler = 'stats.Stats',								name = 'stats'),
])