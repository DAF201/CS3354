from tornado.web import Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from web.path import ROUTE_PATH
from web.auth import account_info_init, ACCOUNTS
from database.database import DATABASE
from web.auth import new_account, fetch_account, update_account
from tools.tools import status_machine
from threading import Thread

if __name__ == '__main__':
    account_info_init()
    t = Thread(target=status_machine)
    t.daemon = True
    t.start()
    # print(ACCOUNTS)
    # new_account('daf201', 'no', 'daf201')
    # update_account('daf201', 'height',  [180, 181, 182, 183])
    # update_account('daf201', 'weight',  [50, 55, 60, 65])
    # update_account('daf201', 'BMI',  [3.5, 4.0, 4.5, 5.0])
    # update_account('daf201', 'workout',  ['run', 'swim', 'walk', 'jog'])
    # update_account('daf201', 'calorie',  [3500, 4000, 3500, 5000])
    # update_account('daf201', 'duration',  [1, 1.5, 4, 2.5])
    # update_account('daf201', 'name',  'Fangzhou Ye', bin=False)
    # DATABASE.commit()
    # print(fetch_account('daf201'))
    app = Application(ROUTE_PATH)
    http_server = HTTPServer(app)
    http_server.listen(80, '0.0.0.0')
    IOLoop.instance().start()
