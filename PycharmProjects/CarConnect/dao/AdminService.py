from entity.IAdminService import IAdminService
from entity.Admin import Admin
from util.DBConnection import DBConnection
from exception.AdminNotFoundException import AdminNotFoundException
from exception.InvalidInputException import InvalidInputException


class AdminService(DBConnection, IAdminService):
    def __init__(self):
        super().__init__()

    def authenticate_admin_data(self, username, password):
        self.open()
        select_query = f"SELECT * FROM Admin WHERE Username LIKE '{username}';"
        self.stmt.execute(select_query)
        admin_data = self.stmt.fetchone()
        if admin_data:
            admin = Admin(*admin_data)
            if admin.authenticate(password):
                print("Authentication successful!")
                self.close()
            else:
                raise AdminNotFoundException("Authentication failed-- Invalid password.")
        else:
            raise AdminNotFoundException("Authentication failed-- Invalid username.")

    def authenticate_admin(self, name):
        if name.isalpha():
            return True
        else:
            raise InvalidInputException("Enter Correct Details...")

    def authenticate_phone(self, phone_number):
        if phone_number.isalnum() and len(phone_number) == 10:
            return True
        else:
            if len(phone_number) != 10:
                raise InvalidInputException("Enter 10 Digit PhoneNo")
            else:
                raise InvalidInputException("Enter Digits only...")

    def register_admin(self):
        admin = Admin()
        try:
            first_name = input("Enter First Name: ")
            if self.authenticate_admin(first_name):
                admin.set_first_name(first_name)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        try:
            last_name = input("Enter Last Name: ")
            if self.authenticate_admin(last_name):
                admin.set_last_name(last_name)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        admin.set_email(input("Enter Email: "))
        try:
            phone_number = input("Enter Phone Number: ")
            if self.authenticate_phone(phone_number):
                admin.set_phone_number(phone_number)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        admin.set_username(input("Enter Username: "))
        admin.set_password(input("Enter Password: "))
        admin.set_role(input("Enter Role: "))
        admin.set_join_date(input("Enter Join Date (YYYY-MM-DD): "))

        data = [(admin.get_first_name(), admin.get_last_name(), admin.get_email(),
                 admin.get_phone_number(), admin.get_username(), admin.get_password(),
                 admin.get_role(), admin.get_join_date())]

        insert_query = '''
        INSERT INTO Admin (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        self.open()
        self.stmt.executemany(insert_query, data)
        self.conn.commit()
        print("Admin registered successfully..")
        self.close()

    def update_admin(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            self.authenticate_admin_data(username, password)
        except AdminNotFoundException as e:
            print(e)
            return
        try:
            self.select_admin()
            admin_id = int(input("Enter AdminID to be updated: "))
            query = f"SELECT AdminID FROM ADMIN WHERE AdminID={admin_id};"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchone()
            if record:
                admin = Admin()
                try:
                    first_name = input("Enter First Name: ")
                    if self.authenticate_admin(first_name):
                        admin.set_first_name(first_name)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                try:
                    last_name = input("Enter Last Name: ")
                    if self.authenticate_admin(last_name):
                        admin.set_last_name(last_name)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                admin.set_email(input("Enter Email: "))
                try:
                    phone_number = input("Enter Phone Number: ")
                    if self.authenticate_phone(phone_number):
                        admin.set_phone_number(phone_number)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                admin.set_username(input("Enter Username: "))
                admin.set_password(input("Enter Password: "))
                admin.set_role(input("Enter Role: "))
                admin.set_join_date(input("Enter Join Date (YYYY-MM-DD): "))

                update_str = '''
                        UPDATE Admin SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, 
                        Username=%s, Password=%s, Role=%s, JoinDate=%s WHERE AdminID=%s
                        '''
                data = [(admin.get_first_name(), admin.get_last_name(), admin.get_email(),
                         admin.get_phone_number(), admin.get_username(), admin.get_password(),
                         admin.get_role(), admin.get_join_date(), admin_id)]
                self.stmt.executemany(update_str, data)
                self.conn.commit()
                print("Admin Updated Successfully...")
                self.close()
            else:
                raise AdminNotFoundException("AdminID not found in Database...")
        except AdminNotFoundException as e:
            print(f"Admin Updation Failed: {e}")

    def delete_admin(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            self.authenticate_admin_data(username, password)
        except AdminNotFoundException as e:
            print(e)
            return
        try:
            admin_id = int(input("Enter AdminID to be deleted: "))
            query = f"SELECT AdminID FROM ADMIN WHERE AdminID={admin_id};"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchone()
            if record:
                delete_str = f'DELETE FROM Admin WHERE AdminID={admin_id};'
                self.open()
                self.stmt.execute(delete_str)
                self.conn.commit()
                print("Admin Deleted Successfully...")
                self.close()
            else:
                raise AdminNotFoundException("AdminID not found in Database...")
        except AdminNotFoundException as e:
            print(f"Admin Not Found: {e}")

    def get_admin_by_id(self):
        try:
            admin_id = int(input("Enter AdminID to get details: "))
            self.open()
            admin_str = f'SELECT * FROM Admin WHERE AdminID={admin_id};'
            self.stmt.execute(admin_str)
            record = self.stmt.fetchone()
            if record:
                print()
                print("...............Admin Details for AdminID: ", admin_id, "...............")
                print(record)
                print()
                self.close()
            else:
                raise AdminNotFoundException("AdminID not found in Database...")
        except AdminNotFoundException as e:
            print(f"Admin Not Found: {e}")

    def get_admin_by_username(self):
        try:
            username = input("Enter Username to get details: ")
            self.open()
            admin_str = f'SELECT * FROM Admin WHERE Username LIKE "{username}";'
            self.stmt.execute(admin_str)
            records = self.stmt.fetchall()
            if records:
                print()
                print("...............Admin Details for Username: ", username, "...............")
                for i in records:
                    print(i)
                print()
                self.conn.commit()
                self.close()
            else:
                raise AdminNotFoundException("Invalid Username...")
        except AdminNotFoundException as e:
            print(f'Admin Not Found: {e}')

    def select_admin(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            self.authenticate_admin_data(username, password)
        except AdminNotFoundException as e:
            print(e)
            return
        self.open()
        select_str = 'SELECT * FROM Admin;'
        self.stmt.execute(select_str)
        records = self.stmt.fetchall()
        print()
        print("...............Records in Admin Table...............")
        for i in records:
            print(i)
        print()
        self.close()
