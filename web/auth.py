from base64 import b64decode, b64encode
from json import dumps, loads
from database.database import DATABASE

ACCOUNTS = {}


def account_info_init():
    buffer = DATABASE.select_all('account')
    for x in buffer:
        ACCOUNTS[x[0]] = x[1]


def new_account(user_name, password, real_name):
    try:
        DATABASE.insert('account', None, (user_name, password))
        DATABASE.insert('name', None, (user_name, real_name))
        DATABASE.insert_bin('BMI',  user_name,
                            b64encode(dumps([]).encode()))
        DATABASE.insert_bin('calorie',  user_name,
                            b64encode(dumps([]).encode()))
        DATABASE.insert_bin('height',  user_name,
                            b64encode(dumps([]).encode()))
        DATABASE.insert_bin('name',  user_name,
                            b64encode(dumps([]).encode()))
        DATABASE.insert_bin('weight',  user_name,
                            b64encode(dumps([]).encode()))
        DATABASE.insert_bin('workout',  user_name,
                            b64encode(dumps([]).encode()))
        DATABASE.commit()
        return {'statu': 201, 'msg': 'success'}
    except Exception as e:
        return {'statu': 403, 'msg': e.__str__()}


def fetch_account(user_name):
    try:
        ac = {}
        ac['password'] = DATABASE.select(
            'account', 'data', 'id=\'%s\'' % user_name)[0][0]
        ac['BMI'] = loads(b64decode(DATABASE.select(
            'BMI', 'data', 'id=\'%s\'' % user_name)[0][0]))
        ac['calorie'] = loads(b64decode(DATABASE.select(
            'calorie', 'data', 'id=\'%s\'' % user_name)[0][0]))
        ac['height'] = loads(b64decode(DATABASE.select(
            'height', 'data', 'id=\'%s\'' % user_name)[0][0]))
        ac['name'] = DATABASE.select(
            'name', 'data', 'id=\'%s\'' % user_name)[0][0]
        ac['weight'] = loads(b64decode(DATABASE.select(
            'weight', 'data', 'id=\'%s\'' % user_name)[0][0]))
        ac['workout'] = loads(b64decode(DATABASE.select(
            'workout', 'data', 'id=\'%s\'' % user_name)[0][0]))
        return {'statu': 200, 'msg': ac.__str__()}

    except Exception as e:
        return {'statu': 403, 'msg': e.__str__()}


def update_account(user_name, table, value, bin=True):
    try:
        DATABASE.update_bin(table, user_name, b64encode(dumps(value).encode())) if bin else DATABASE.update(
            table, user_name, value)
        DATABASE.commit()
        return {'statu': 200, 'msg': 'success'}
    except Exception as e:
        print(e)
        return {'statu': 304, 'msg': e.__str__()}
