class Vehicle:
    def __init__(self, vehicle_id=None, model=None, make=None, year=None,
                 color=None, registration_number=None, availability=None, daily_rate=None):
        self.__vehicle_id = vehicle_id
        self.__model = model
        self.__make = make
        self.__year = year
        self.__color = color
        self.__registration_number = registration_number
        self.__availability = availability
        self.__daily_rate = daily_rate

    # Getters
    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_model(self):
        return self.__model

    def get_make(self):
        return self.__make

    def get_year(self):
        return self.__year

    def get_color(self):
        return self.__color

    def get_registration_number(self):
        return self.__registration_number

    def get_availability(self):
        return self.__availability

    def get_daily_rate(self):
        return self.__daily_rate

    # Setters
    def set_model(self, model):
        self.__model = model

    def set_make(self, make):
        self.__make = make

    def set_year(self, year):
        self.__year = year

    def set_color(self, color):
        self.__color = color

    def set_registration_number(self, registration_number):
        self.__registration_number = registration_number

    def set_availability(self, availability):
        self.__availability = availability

    def set_daily_rate(self, daily_rate):
        self.__daily_rate = daily_rate
