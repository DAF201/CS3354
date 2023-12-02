from tornado.web import RequestHandler
from web.static_file import *
from tornado_http_auth import auth_required, DigestAuthMixin
from web.auth import ACCOUNTS, new_account, fetch_account, update_account
from GUI.diagram import draw, draw_all
from re import search
from base64 import b64encode
from json import loads


class root(RequestHandler):
    def get(self):
        return self.write(STATIC_FILES['home.html'])


class APIs(RequestHandler, DigestAuthMixin):
    def __init__(self, application, request, **kwargs) -> None:
        super().__init__(application, request, **kwargs)

        # handle different params using the same URL(to make less classes)
        self.API_handlers = {
            'post': {
                '/API?account_register': self.account_register_post,
                '/API?account_logout': self.account_logout,
                '/API?account_log_update': self.account_log_update,
                '/API?statistic_analysis_b64': self.account_statistic_b64,

            },
            # try to void use get, get does not hide params
            'get': {
                '/API?account_logging': self.account_logging,
                '/API?statistic_analysis': self.account_statistic,
                '/API?account_register': self.account_register_get,
            }
        }

    def get(self, *args):
        self.API_handlers['get'][self.request.uri]()

    def post(self, *args):
        self.API_handlers['post'][self.request.uri]()

    def account_register_get(self, *args):
        self.write(STATIC_FILES['account_registration.html'])

    def account_register_post(self, *args):
        print(self.request.body_arguments)
        user_name = self.request.body_arguments['name'][0].decode()
        email = self.request.body_arguments['email'][0].decode()
        password = self.request.body_arguments['password'][0].decode()
        print(new_account(user_name, password, email))
        self.write(STATIC_FILES['redirect.html'])

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_logging(self, *args):
        self.write(STATIC_FILES['data_logging.html'])

    def account_log_update(self, *args):
        user = search('username=\".*\", realm', self.request.headers.get('Authorization')
                      ).group(0).replace('username="', '').replace('", realm', '')
        data = fetch_account(user)['msg']
        print(self.request.body_arguments)
        typing = self.request.body_arguments['type'][0].decode()
        if typing == 'workout':
            typing = 'duration'
        try:
            value = float(self.request.body_arguments['value'][0].decode())
            data[typing].append(value)
        except Exception as e:
            print(e)
            data[typing].append(0)
        d = update_account(user, typing, data[typing])
        print(d)
        self.write('okay')

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_statistic(self):
        user = search('username=\".*\", realm', self.request.headers.get('Authorization')
                      ).group(0).replace('username="', '').replace('", realm', '')
        self.write(draw_all(user))

    @auth_required(realm='Protected', auth_func=ACCOUNTS.get)
    def account_statistic_b64(self):
        options = ['height', 'weight', 'calorie', 'BMI', 'duration']
        key = []
        for x in self.request.body_arguments.keys():
            key.append(x)
        data = loads(key[0])
        user = search('username=\".*\", realm', self.request.headers.get('Authorization')
                      ).group(0).replace('username="', '').replace('", realm', '')
        self.write(b64encode(draw(user, options[int(data) % 5])))

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
