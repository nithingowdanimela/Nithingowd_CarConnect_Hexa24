from entity.IReservationService import IReservationService
from entity.Reservation import Reservation
from util.DBConnection import DBConnection
from exception.ReservationException import ReservationException
from exception.InvalidInputException import InvalidInputException
from datetime import datetime


class ReservationService(DBConnection, IReservationService):
    def __init__(self):
        super().__init__()

    def is_vehicle_reserved(self, vehicle_id, start_date):
        select_query = f"SELECT * FROM Reservation WHERE VehicleID = {vehicle_id} AND EndDate<'{start_date}' ORDER BY ENdDate DESC LIMIT 1;"
        self.open()
        self.stmt.execute(select_query)
        result = self.stmt.fetchall()
        self.close()
        if result:
            return True
        else:
            return False

    def authenticate_id(self, id):
        if id.isdigit():
            return True
        else:
            raise InvalidInputException("Enter Correct Id...")

    def create_reservation(self):
        try:
            reservation = Reservation()
            try:
                customer_id = input("Enter customerID: ")
                if self.authenticate_id(customer_id):
                    reservation.set_customer_id(customer_id)
            except InvalidInputException as e:
                print(f'Invalid Input: {e}')
            try:
                vehicle_id = input("Enter VehicleID: ")
                if self.authenticate_id(vehicle_id):
                    reservation.set_vehicle_id(vehicle_id)
            except InvalidInputException as e:
                print(f'Invalid Input: {e}')
            start_date_str = input("Enter Start Date {YYYY-MM-DD}: ")
            end_date_str = input("Enter End Date {YYYY-MM-DD}: ")
            # Convert string dates to MySQL date format
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
            reservation.set_start_date(start_date)
            reservation.set_end_date(end_date)
            reservation.set_status(input("Enter Status: "))
            self.open()
            daily_query = f"SELECT DailyRate FROM Vehicle WHERE VehicleID={reservation.get_vehicle_id()};"
            self.stmt.execute(daily_query)
            daily_rate = self.stmt.fetchone()[0]
            reservation.set_daily_rate(daily_rate)
            total_cost = float(reservation.calculate_total_cost())
            data = [reservation.get_customer_id(), reservation.get_vehicle_id(), reservation.get_start_date(),
                    reservation.get_end_date(), total_cost, reservation.get_status()]
            if not self.is_vehicle_reserved(reservation.get_vehicle_id(), reservation.get_start_date()):
                raise ReservationException("Vehicle is already reserved")
            insert_query = '''
            INSERT INTO Reservation (customerID, VehicleID, StartDate, EndDate, TotalCost, Status)
            VALUES (%s, %s, %s, %s, %s, %s);
            '''
            self.stmt.execute(insert_query, data)
            self.conn.commit()
            print("Reservation created successfully..")
            self.close()
        except ReservationException as e:
            print(f"Reservation Failed: {e}")

    def update_reservation(self):
        try:
            self.select_reservation()
            reservation_id = int(input("Enter ReservationID to be updated: "))
            query = f"SELECT ReservationID FROM Reservation WHERE ReservationID={reservation_id}"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchone()
            if record:
                reservation = Reservation()
                try:
                    customer_id = input("Enter customerID: ")
                    if self.authenticate_id(customer_id):
                        reservation.set_customer_id(customer_id)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                try:
                    vehicle_id = input("Enter VehicleID: ")
                    if self.authenticate_id(vehicle_id):
                        reservation.set_vehicle_id(vehicle_id)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                start_date_str = input("Enter Start Date {YYYY-MM-DD}: ")
                end_date_str = input("Enter End Date {YYYY-MM-DD}: ")
                # Convert string dates to MySQL date format
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').strftime('%Y-%m-%d')
                reservation.set_start_date(start_date)
                reservation.set_end_date(end_date)
                reservation.set_status(input("Enter Status: "))
                self.open()
                daily_query = f"SELECT DailyRate FROM Vehicle WHERE VehicleID={reservation.get_vehicle_id()};"
                self.stmt.execute(daily_query)
                daily_rate = self.stmt.fetchone()[0]
                reservation.set_daily_rate(daily_rate)
                total_cost = float(reservation.calculate_total_cost())
                update_str = ('''
                        UPDATE Reservation SET customerID=%s, VehicleID=%s, StartDate=%s, EndDate=%s, TotalCost=%s,
                        Status=%s WHERE ReservationID=%s;
                        ''')
                data = [(reservation.get_customer_id(), reservation.get_vehicle_id(), reservation.get_start_date(),
                         reservation.get_end_date(), total_cost, reservation.get_status(),
                         reservation_id)]
                self.stmt.executemany(update_str, data)
                self.conn.commit()
                print("Reservation Updated Successfully...")
                self.close()
            else:
                raise ReservationException("Invalid ReservationID...")
        except ReservationException as e:
            print(f"Reservation Update Failed: {e}")

    def cancel_reservation(self):
        try:
            reservation_id = int(input("Enter ReservationID to be canceled: "))
            query = f"SELECT ReservationID FROM Reservation WHERE ReservationID={reservation_id}"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchone()
            if record:
                delete_str = f'DELETE FROM Reservation WHERE ReservationID={reservation_id};'
                self.stmt.execute(delete_str)
                self.conn.commit()
                print("Reservation Canceled Successfully...")
                self.close()
            else:
                raise ReservationException("Invalid ReservationID...")
        except ReservationException as e:
            print(f"Reservation Cancellation Failed: {e}")

    def get_reservation_by_id(self):
        try:
            reservation_id = int(input("Enter ReservationID to get details: "))
            query = f"SELECT ReservationID FROM Reservation WHERE ReservationID={reservation_id};"
            self.open()
            self.stmt.execute(query)
            #self.stmt.execute(query, (reservation_id,))
            record = self.stmt.fetchone()
            if record:
                reservation_str = f'SELECT * FROM Reservation WHERE ReservationID={reservation_id};'
                self.stmt.execute(reservation_str)
                records = self.stmt.fetchall()
                print()
                print("...............Reservation Details for ReservationID: ", reservation_id, "...............")
                for i in records:
                    print(i)
                print()
                self.conn.commit()
                self.close()
            else:
                raise ReservationException("Invalid ReservationID...")
        except ReservationException as e:
            print(f"Reservation Exception: {e}")

    def get_reservations_by_customer_id(self):
        try:
            customer_id = int(input("Enter customerID to get reservations: "))
            query = f"SELECT CustomerId FROM Reservation WHERE customerID={customer_id};"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchall()
            if record:
                reservation_str = f'SELECT * FROM Reservation WHERE customerID={customer_id};'
                self.stmt.execute(reservation_str)
                records = self.stmt.fetchall()
                print()
                print("...............Reservations for customerID:", customer_id, "...............")
                for i in records:
                    print(i)
                print()
                self.conn.commit()
                self.close()
            else:
                raise ReservationException("Invalid customerID...")
        except ReservationException as e:
            print(f"Reservation Exception: {e}")

    def select_reservation(self):
        self.open()
        select_str = 'SELECT * FROM Reservation;'
        self.stmt.execute(select_str)
        records = self.stmt.fetchall()
        print()
        print("...............Records in Reservation Table...............")
        for i in records:
            print(i)
        print()
        self.close()


'''
# from Interface.Implements import implements
from entity.IReservationService import IReservationService


class ReservationService(IReservationService):
    def __init__(self, reservation_repository):
        self.reservation_repository = reservation_repository

    def get_reservation_by_id(self, reservation_id):
        return self.reservation_repository.get_reservation_by_id(reservation_id)

    def get_reservations_by_customer_id(self, customer_id):
        return self.reservation_repository.get_reservations_by_customer_id(customer_id)

    def create_reservation(self, reservation):
        return self.reservation_repository.create_reservation(reservation)

    def update_reservation(self, reservation_id, new_reservation_data):
        return self.reservation_repository.update_reservation(reservation_id, new_reservation_data)

    def cancel_reservation(self, reservation_id):
        return self.reservation_repository.cancel_reservation(reservation_id)
'''
