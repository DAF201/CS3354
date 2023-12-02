from gc import collect
from time import sleep
from database.database import DATABASE
from web.auth import ACCOUNTS
STATUS = 0


def cleanup():
    collect()
    global STATUS
    if (STATUS == len(MOVES)-1):
        STATUS = 0
    else:
        STATUS += 1


def check_update():
    DATABASE.commit()

    global STATUS
    if (STATUS == len(MOVES)-1):
        STATUS = 0
    else:
        STATUS += 1


def update_account():
    global ACCOUNTS
    try:
        buffer = DATABASE.select_all('account')
        for x in buffer:
            ACCOUNTS[x[0]] = x[1]
        # print(ACCOUNTS)
    except:
        pass

    global STATUS
    if (STATUS == len(MOVES)-1):
        STATUS = 0
    else:
        STATUS += 1


MOVES = [cleanup, check_update, update_account]


def status_machine():
    global STATUS
    while (1):
        MOVES[STATUS]()
        sleep(1)
