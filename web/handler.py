from tornado.web import RequestHandler
from web.static_file import *
from tornado_http_auth import auth_required, DigestAuthMixin
from web.auth import ACCOUNTS, new_account, fetch_account, update_account
from GUI.diagram import draw
from re import search


class root(RequestHandler):
    def get(self):
        return self.write(STATIC_FILES['home.html'])


class APIs(RequestHandler, DigestAuthMixin):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)

        # handle different params using the same URL(to make less classes)
        self.API_handlers = {
            'post': {
                '/API?account_register': self.account_registion,
                '/API?account_home': self.account_home,
                '/API?account_logout': self.account_logout,
                '/API?account_log_update': self.account_log_update
            },
            # try to void use get, get does not hide params
            'get': {
                '/API?account_logging': self.account_logging,
                '/API?statistic_analysis': self.account_statistic
            }
        }

    def get(self, *args):
        self.API_handlers['get'][self.request.uri]()

    def post(self, *args):
        self.API_handlers['post'][self.request.uri]()

    def account_registion(self, *args):
        pass

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_home(self, *args):
        pass

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_logging(self, *args):
        self.write(STATIC_FILES['data_logging.html'])

    def account_log_update(self, *args):

        self.write('')

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_statistic(self):
        user = search('username=\".*\", realm', self.request.headers.get('Authorization')
                      ).group(0).replace('username="', '').replace('", realm', '')
        user_data = fetch_account(user)
        self.write(draw('test', 'lb', user_data['msg']['duration']))

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_logout(self, *args):
        self.clear()
        self.set_status(401)
        self.finish(STATIC_FILES['logout_page.html'])


class STATIC(RequestHandler):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)

    def post(self, *args):
        self.clear()
        self.set_status(403)
        self.finish("<html><body>METHOD FORBIDDEN</body></html>")
        return

    def get(self, *args):
        try:
            self.write(
                STATIC_FILES[self.request.arguments['file'][0].decode()])
            return
        except Exception as e:
            print(e)
            self.clear()
            self.set_status(404)
            self.finish("<html><body>NO FOUND</body></html>")
            return
