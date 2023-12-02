from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from web.path import ROUTE_PATH
from web.auth import account_info_init, ACCOUNTS
from database.database import DATABASE
from web.auth import new_account, fetch_account, update_account

if __name__ == '__main__':
    account_info_init()
    print(ACCOUNTS)
    # new_account('daf201', '', 'daf201')
    # update_account('daf201', 'height',  [100, 110, 120, 130])
    # update_account('daf201', 'weight',  [50, 55, 60])
    # update_account('daf201', 'BMI',  [3, 4, 4.5])
    # update_account('daf201', 'workout',  [2.5, 2.5, 3.5])
    # update_account('daf201', 'name',  'none', bin=False)
    # update_account('daf201', 'duration')
    # DATABASE.commit()
    print(fetch_account('daf201'))
    app = Application(ROUTE_PATH)
    http_server = HTTPServer(app)
    http_server.listen(80, '0.0.0.0')
    IOLoop.instance().start()
