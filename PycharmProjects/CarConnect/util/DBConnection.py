import mysql.connector as sql


class DBConnection:

    def __init__(self, host='localhost', database='CarConnect', user='root', password='Nithin@2003'):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.conn = None
        self.stmt = None

    def open(self):
        try:
            self.conn = sql.connect(host='localhost', database='CarConnect', user='root', password='Nithin@2003')
            # connecting with database
            if self.conn.is_connected():
                print("Database Is Connected....")
                self.conn.commit()
            else:
                print("Not Connected with Database....")
            self.stmt = self.conn.cursor()
        except Exception as e:
            print(str(e) + "DB Not connected...")

    def close(self):
        self.conn.close()
        print("Database Connection is Closed...")


obj = DBConnection()
obj.open()
obj.close()
