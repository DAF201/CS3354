from tornado.web import RequestHandler
from web.static_file import *
from tornado_http_auth import auth_required, DigestAuthMixin


class root(RequestHandler):
    def get(self):
        return self.write(STATIC_FILES['home.html'])


class APIs(RequestHandler, DigestAuthMixin):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)

        # handle different params using the same URL
        self.API_handlers = {
            'post': {
                '/API?account_register': self.account_registion
            },
            'get': {
                '/API?account_home': self.account_home,
                '/API?account_info': self.account_home,
                '/API?account_logout': self.account_logout
            }
        }

    def get(self):
        self.API_handlers['get'][self.request.uri]()

    def post(self):
        self.API_handlers['post'][self.request.uri]()

    def account_registion(self):
        pass

    # @auth_required()
    def account_home(self):
        pass

    def account_logout(self):
        pass


class STATIC(RequestHandler):
    pass
