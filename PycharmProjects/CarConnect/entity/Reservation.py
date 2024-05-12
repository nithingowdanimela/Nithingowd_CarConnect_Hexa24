class Reservation:
    def __init__(self, reservation_id=None, customer_id=None, vehicle_id=None, start_date=None,
                 end_date=None, daily_rate=None, total_cost=None, status=None):
        self.__reservation_id = reservation_id
        self.__customer_id = customer_id
        self.__vehicle_id = vehicle_id
        self.__start_date = start_date
        self.__end_date = end_date
        self.__daily_rate = daily_rate
        self.__total_cost = total_cost
        self.__status = status

    # Getters
    def get_reservation_id(self):
        return self.__reservation_id

    def get_customer_id(self):
        return self.__customer_id

    def get_vehicle_id(self):
        return self.__vehicle_id

    def get_start_date(self):
        return self.__start_date

    def get_end_date(self):
        return self.__end_date

    def get_daily_rate(self):
        return self.__daily_rate

    def get_total_cost(self):
        return self.__total_cost

    def get_status(self):
        return self.__status

    # Setters
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def set_start_date(self, start_date):
        self.__start_date = start_date

    def set_end_date(self, end_date):
        self.__end_date = end_date

    def set_daily_rate(self, daily_rate):
        self.__daily_rate = daily_rate

    def set_total_cost(self, total_cost):
        self.__total_cost = total_cost

    def set_status(self, status):
        self.__status = status

    # Method to calculate total cost
    def calculate_total_cost(self):
        from datetime import datetime

        if self.__start_date and self.__end_date:
            start_date = datetime.strptime(self.__start_date, '%Y-%m-%d')
            end_date = datetime.strptime(self.__end_date, '%Y-%m-%d')
            num_days = (end_date - start_date).days
            total_cost = (num_days+1) * self.__daily_rate
            return total_cost
        else:
            return 0
