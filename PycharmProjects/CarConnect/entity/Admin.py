class Admin:
    def __init__(self, admin_id=None, first_name=None, last_name=None, email=None,
                 phone_number=None, username=None, password=None, role=None, join_date=None):
        self.__admin_id = admin_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__phone_number = phone_number
        self.__username = username
        self.__password = password
        self.__role = role
        self.__join_date = join_date

    # Getters
    def get_admin_id(self):
        return self.__admin_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    def get_phone_number(self):
        return self.__phone_number

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_role(self):
        return self.__role

    def get_join_date(self):
        return self.__join_date

    # Setters
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email(self, email):
        self.__email = email

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_username(self, username):
        self.__username = username

    def set_password(self, password):
        self.__password = password

    def set_role(self, role):
        self.__role = role

    def set_join_date(self, join_date):
        self.__join_date = join_date

    # Method to authenticate password
    def authenticate(self, password):
        return self.__password == password
