#!./env/bin/python

#################################
#                               #
#      Tornado server init      #
#                               #
#################################

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from sosconf import app

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()