from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from web.path import ROUTE_PATH
from web.auth import account_info_init
if __name__ == '__main__':
    app = Application(ROUTE_PATH)
    http_server = HTTPServer(app)
    http_server.listen(80)
    IOLoop.instance().start()
