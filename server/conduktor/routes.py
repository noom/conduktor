import os

from tornado.web import RedirectHandler as TornadoRedirectHandler
from tornado.web import StaticFileHandler

from conduktor.handlers.client_vars import ClientVarsHandler
from conduktor.handlers.health import HealthHandler
from conduktor.handlers.logs import URLLogHandler
from conduktor.handlers.redirect import RedirectHandler
from conduktor.handlers.url import URLHandler


routes = [
    (r'^/$', TornadoRedirectHandler, {'url' : '/_/index.html'}),
    (r'^/_(/?)$', TornadoRedirectHandler, {'url' : '/_/index.html'}),
    (r'^/_/api/v1/url/(?P<url_id>\d+)/logs$', URLLogHandler),
    (r'^/_/api/v1/url/(?P<url_id>\d+)$', URLHandler),
    (r'^/_/api/v1/url/?$', URLHandler),
    (r'^/_/health/?$', HealthHandler),
    (r'^/(?P<slug>[a-z0-9][a-z0-9\_\-]*)$', RedirectHandler),
    (r'^/_/env.js$', ClientVarsHandler), 
    (r'^/_/(.*)$', StaticFileHandler, {'path' : os.path.join(os.path.dirname(__file__), 'static')}),
]  
