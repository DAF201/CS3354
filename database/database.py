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
        if values == None or table == None:
            return False
        try:
            op = 'INSERT INTO ' + table
            if cols != None:
                op += '('
                op += ','.join(cols)
                op = op+') VALUES('
            else:
                op = op+' VALUES('
            for value in values:
                if type(value) == str and ('SELECT' not in value):
                    op += "'"+value+"',"
                else:
                    op += str(value)+','
            op = op[:-1]+');'
            self.cursor.execute(op)
            return True

        except Exception as e:
            print(e)
            return False

    # binary
    def insert_bin(self, table, chunk_id, value: bytes):
        if any([x == None for x in (table, value)]):
            return False
        try:
            op = 'INSERT INTO '+'%s(chunk_id,data)' % table + \
                ' VALUES(\''+chunk_id+'\',%s);'
            self.cursor.execute(op, (value,))
            return True
        except Exception as e:
            print(e)
            return False

    def select(self, table, col, where):
        try:
            if any([x == None for x in [table, col, where]]):
                return False
            op = "SELECT %s FROM %s WHERE %s" % (col, table, where)
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

    def update(self, table, primary_key, what):
        try:
            op = 'UPDATE %s SET %s WHERE id=\'%s\'' % (
                table, what, primary_key)
            self.cursor.execute(op)
            return True
        except Exception as e:
            print(e)
            return None

    def commit(self):
        self.database.commit()
