from gc import collect
from time import sleep
from database.database import DATABASE
STATUS = 0


def cleanup():
    collect()
    # print('collecting garbage')
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


MOVES = [cleanup, check_update]


def status_machine():
    global STATUS
    while (1):
        MOVES[STATUS]()
        sleep(5)
