from entity.ICustomerService import ICustomerService
from entity.Customer import Customer
from util.DBConnection import DBConnection
from exception.AuthenticationException import AuthenticationException
from exception.InvalidInputException import InvalidInputException


class CustomerService(DBConnection, ICustomerService):
    def __init__(self):
        super().__init__()

    def authenticate_customer_data(self, username, password):
        self.open()
        select_query = f"SELECT * FROM Customer WHERE Username LIKE '{username}';"
        self.stmt.execute(select_query)
        customer_data = self.stmt.fetchone()
        if customer_data:
            customer = Customer(*customer_data)
            if customer.authenticate(password):
                print("Authentication Successful!")
                self.close()
            else:
                raise AuthenticationException("Authentication failed-- Invalid password.")
        else:
            raise AuthenticationException("Authentication failed-- Invalid username.")

    def authenticate_customer_test(self, username, password):
        self.open()
        select_query = f"SELECT * FROM Customer WHERE Username LIKE '{username}';"
        self.stmt.execute(select_query)
        customer_data = self.stmt.fetchone()
        if customer_data:
            customer = Customer(*customer_data)
            if customer.authenticate(password):
                return "Authentication Successful!"
            else:
                return "Authentication failed-- Invalid password."
        else:
            return "Authentication failed-- Invalid username."

    def authenticate_customer_(self, name):
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

    def register_customer(self):
        customer = Customer()
        try:
            first_name = input("Enter First Name of Customer: ")
            if self.authenticate_customer_(first_name):
                customer.set_first_name(first_name)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        try:
            last_name = input("Enter Last Name of Customer: ")
            if self.authenticate_customer_(last_name):
                customer.set_last_name(last_name)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        customer.set_email(input("Enter Email of Customer: "))
        try:
            phone_number = input("Enter Phone Number of Customer: ")
            if self.authenticate_phone(phone_number):
                customer.set_phone_number(phone_number)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        customer.set_address(input("Enter Address of Customer: "))
        customer.set_username(input("Enter Username of Customer: "))
        customer.set_password(input("Enter Password of Customer: "))
        customer.set_registration_date(input("Enter Registration Date {YYYY-MM-DD}: "))

        data = [(customer.get_first_name(), customer.get_last_name(), customer.get_email(),
                 customer.get_phone_number(), customer.get_address(), customer.get_username(),
                 customer.get_password(), customer.get_registration_date())]
        insert_query = '''
        INSERT INTO Customer (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        self.open()
        self.stmt.executemany(insert_query, data)
        self.conn.commit()
        print("Records inserted successfully..")
        self.close()

    def update_customer(self):
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        try:
            self.authenticate_customer_data(username, password)
        except InvalidInputException as e:
            print(e)
            return
        self.select_customers()
        customer_id = int(input("Enter customerID to be updated: "))
        customer = Customer()
        try:
            first_name = input("Enter First Name of Customer: ")
            if self.authenticate_customer_(first_name):
                customer.set_first_name(first_name)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        try:
            last_name = input("Enter Last Name of Customer: ")
            if self.authenticate_customer_(last_name):
                customer.set_last_name(last_name)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        customer.set_email(input("Enter Email of Customer: "))
        try:
            phone_number = input("Enter Phone Number of Customer: ")
            if self.authenticate_phone(phone_number):
                customer.set_phone_number(phone_number)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        customer.set_address(input("Enter Address: "))
        update_str = ('''
                UPDATE Customer SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s WHERE customerID=%s;
                ''')
        self.open()
        data = [(customer.get_first_name(), customer.get_last_name(), customer.get_email(), customer.get_phone_number(),
                 customer.get_address(), customer_id)]
        self.stmt.executemany(update_str, data)
        self.conn.commit()
        print("Records Updated Successfully...")
        self.close()
        return "Records Updated Successfully..."

    def delete_customer(self):
        try:
            Id = int(input("Enter customerID to be deleted: "))
            select_query = "SELECT * FROM Customer WHERE customerID = %s"
            self.open()
            self.stmt.execute(select_query, (Id,))
            customer_data = self.stmt.fetchone()
            if customer_data:
                delete_str = f'DELETE FROM Customer WHERE customerID={Id};'
                self.open()
                self.stmt.execute(delete_str)
                self.conn.commit()
                print("Records Deleted Successfully...")
                self.close()
            else:
                raise InvalidInputException("customerID not found in Database...")
        except InvalidInputException as e:
            print(f"Customer Deletion Failed: {e}")

    def get_customer_by_id(self):
        try:
            customer_id = int(input("Enter CustomerId to get details: "))
            self.open()
            cus_str = f'SELECT * FROM Customer WHERE CustomerId={customer_id};'
            self.stmt.execute(cus_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                print()
                print("...............Customer Details for customerID: ", customer_id, "...............")
                for i in records:
                    print(i)
                print()
                self.close()
            else:
                raise InvalidInputException("customerID not found in Database...")
        except InvalidInputException as e:
            print(f"Customer Not Found: {e}")

    def get_customer_by_username(self):
        try:
            username = input("Enter UserName to get details: ")
            self.open()
            username_str = f"SELECT * FROM Customer WHERE UserName LIKE '{username}';"
            self.stmt.execute(username_str)
            records = self.stmt.fetchall()
            self.conn.commit()
            if records:
                print()
                print("...............Customer Details for Username: ", username, "...............")
                for i in records:
                    print(i)
                print()
                self.close()
            else:
                raise InvalidInputException("Invalid Username...")
        except InvalidInputException as e:
            print(f"Customer Not Found: {e}")

    def select_customers(self):
        self.open()
        select_str = 'SELECT * FROM Customer;'
        self.stmt.execute(select_str)
        records = self.stmt.fetchall()
        print()
        print("...............Records in Table...............")
        for i in records:
            print(i)
        print()
        self.close()
