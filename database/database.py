from mysql import connector
from json import load


class database:
    def __init__(self) -> None:
        try:
            with open(r'./database/config.json')as config:
                config = load(config)
                if any([x == '' for x in (config[y] for y in config.keys())]):
                    self.database = connector.connect(
                        host=input('enter host:\n'),
                        port=int(input('enter port:\n')),
                        user=input('enter user:\n'),
                        password=input('enter password:\n')
                    )
                else:
                    self.database = connector.connect(
                        host=config['host'],
                        port=config['port'],
                        user=config['user'],
                        password=config['password']
                    )
            self.cursor = self.database.cursor()
            if config['database']:
                self.cursor.execute("use %s;" % config['database'])
            else:
                self.cursor.execute("use %s;" % input('enter database:\n'))
            print(self.database.get_server_info())
        except Exception as e:
            print(e)
            exit()

    # str and int
    def insert(self, table, cols, values):
        if values is None or table is None:
            return False
        try:
            op = 'INSERT INTO ' + table
            if cols is not None:
                if type(cols) != str:
                    op += '('
                    op += ','.join(cols)
                    op = op+') VALUES('
                else:
                    op += '(%s) VALUES(' % cols
            else:
                op = op+' VALUES('
            if type(values) != str:
                for value in values:
                    if type(value) == str and ('SELECT' not in value):
                        op += "'"+value+"',"
                    else:
                        op += str(value)+','
            else:
                op += "\'%s\'\'" % values
            op = op[:-1]+');'
            print(op)
            self.cursor.execute(op)
            return True

        except Exception as e:
            print(e)
            return False

    # binary
    def insert_bin(self, table, id, value: bytes):
        if any([x is None for x in (table, value)]):
            return False
        try:
            op = 'INSERT INTO '+'%s(id,data)' % table + \
                ' VALUES(\''+id+'\',%s);'
            self.cursor.execute(op, (value,))
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, table, col, where):
        try:
            if any([x is None for x in [table, col, where]]):
                return False
            op = "SELECT %s FROM %s WHERE %s" % (col, table, where)
            print(op)
            self.cursor.execute(op)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return None

    def select_all(self, table):
        try:
            self.cursor.execute("SELECT * FROM %s;" % table)
            return self.cursor.fetchall()
        except Exception as e:
            print(e)
            return None

    def update(self, table, primary_key, value):
        try:
            op = 'UPDATE %s SET data=\'%s\' WHERE id=\'%s\';' % (
                table, value, primary_key)
            print(op)
            self.cursor.execute(op)
            return True
        except Exception as e:
            print(e)
            return None

    def update_bin(self, table, primary_key, value):
        try:
            op = 'UPDATE ' + table+' SET data=%s '+' WHERE id=\''+primary_key+'\';'
            print(op)
            self.cursor.execute(op, (value,))
            return True
        except Exception as e:
            print(e)
            return None

    def commit(self):
        self.database.commit()


DATABASE = database()
