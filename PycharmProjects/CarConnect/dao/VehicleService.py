from entity.IVehicleService import IVehicleService
from entity.Vehicle import Vehicle
from util.DBConnection import DBConnection
from exception.VehicleNotFoundException import VehicleNotFoundException
from exception.InvalidInputException import InvalidInputException


class VehicleService(DBConnection, IVehicleService):
    def __init__(self):
        super().__init__()

    def authenticate_name(self, name):
        if name.isalpha():
            return True
        else:
            raise InvalidInputException("Enter Correct Details...")

    def add_vehicle(self):
        vehicle = Vehicle()
        try:
            model = input("Enter Model of Vehicle: ")
            if self.authenticate_name(model):
                vehicle.set_model(model)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        try:
            make = input("Enter Make of Vehicle: ")
            if self.authenticate_name(make):
                vehicle.set_make(make)
        except InvalidInputException as e:
            print(f'Invalid Input: {e}')
            return
        vehicle.set_year(int(input("Enter Year of Vehicle: ")))
        vehicle.set_color(input("Enter Color of Vehicle: "))
        vehicle.set_registration_number(input("Enter Registration Number of Vehicle: "))
        vehicle.set_availability(True if input("Is Vehicle Available? (yes/no): ").lower() == 'yes' else False)
        vehicle.set_daily_rate(float(input("Enter Daily Rate of Vehicle: ")))

        data = [(vehicle.get_model(), vehicle.get_make(), vehicle.get_year(), vehicle.get_color(),
                 vehicle.get_registration_number(), vehicle.get_availability(), vehicle.get_daily_rate())]

        insert_query = '''
        INSERT INTO Vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
        '''
        self.open()
        self.stmt.executemany(insert_query, data)
        self.conn.commit()
        print("Vehicle added successfully...")
        self.close()
        return "Vehicle added successfully..."

    def update_vehicle(self):
        try:
            self.select_vehicle()
            vehicle_id = int(input("Enter VehicleID to be updated: "))
            query = f"SELECT VehicleID FROM Vehicle WHERE VehicleID={vehicle_id};"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchone()
            if record:
                vehicle = Vehicle()
                try:
                    model = input("Enter Model of Vehicle: ")
                    if self.authenticate_name(model):
                        vehicle.set_model(model)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                try:
                    make = input("Enter Make of Vehicle: ")
                    if self.authenticate_name(make):
                        vehicle.set_make(make)
                except InvalidInputException as e:
                    print(f'Invalid Input: {e}')
                    return
                vehicle.set_year(int(input("Enter Year: ")))
                vehicle.set_color(input("Enter Color: "))
                vehicle.set_registration_number(input("Enter Registration Number: "))
                vehicle.set_availability(True if input("Is Vehicle Available? (yes/no): ").lower() == 'yes' else False)
                vehicle.set_daily_rate(float(input("Enter Daily Rate: ")))

                update_str = '''
                        UPDATE Vehicle SET Model=%s, Make=%s, Year=%s, Color=%s, RegistrationNumber=%s, Availability=%s,
                        DailyRate=%s WHERE VehicleID=%s;
                        '''
                data = [(vehicle.get_model(), vehicle.get_make(), vehicle.get_year(), vehicle.get_color(),
                         vehicle.get_registration_number(), vehicle.get_availability(), vehicle.get_daily_rate(), vehicle_id)]
                self.stmt.executemany(update_str, data)
                self.conn.commit()
                print("Vehicle Updated Successfully...")
                self.close()
                return "Vehicle Updated Successfully..."
            else:
                raise VehicleNotFoundException("Invalid VehicleID...")
        except VehicleNotFoundException as e:
            print(f"Vehicle Updation Failed: {e}")

    def remove_vehicle(self):
        try:
            vehicle_id = int(input("Enter VehicleID to be deleted: "))
            query = f"SELECT VehicleID FROM Vehicle WHERE VehicleID={vehicle_id};"
            self.open()
            self.stmt.execute(query)
            record = self.stmt.fetchone()
            if record:
                delete_str = f'DELETE FROM Vehicle WHERE VehicleID={vehicle_id}'
                self.stmt.execute(delete_str)
                self.conn.commit()
                print("Vehicle Deleted Successfully...")
                self.close()
            else:
                raise VehicleNotFoundException("Invalid VehicleID...")
        except VehicleNotFoundException as e:
            print(f"Vehicle Removal Failed: {e}")

    def get_vehicle_by_id(self):
        try:
            vehicle_id = int(input("Enter VehicleID to get details: "))
            self.open()
            vehicle_str = f'SELECT * FROM Vehicle WHERE VehicleID={vehicle_id};'
            self.stmt.execute(vehicle_str)
            record = self.stmt.fetchone()
            self.conn.commit()
            if record:
                print()
                print("...............Vehicle Details for VehicleID: ", vehicle_id, "...............")
                print(record)
                print()
                self.close()
            else:
                raise VehicleNotFoundException("Invalid VehicleID...")
        except VehicleNotFoundException as e:
            print(f"Vehicle Not Found: {e}")

    def get_available_vehicles(self):
        self.open()
        vehicle_str = 'SELECT * FROM Vehicle v JOIN Reservation r ON v.VehicleID=r.VehicleID WHERE r.EndDate<CURDATE();'
        self.stmt.execute(vehicle_str)
        records = self.stmt.fetchall()
        print()
        print("...............Available Vehicles...............")
        if records:
            for i in records:
                print(i)
                return True
            print()
        self.conn.commit()
        self.close()

    def select_vehicle(self):
        self.open()
        select_str = 'SELECT * FROM Vehicle;'
        self.stmt.execute(select_str)
        records = self.stmt.fetchall()
        print()
        print("...............Records in Vehicle Table...............")
        if records:
            for i in records:
                print(i)
            return True
        print()
        self.close()


'''

class VehicleService(IVehicleService):
    def __init__(self, vehicle_repository):
        self.vehicle_repository = vehicle_repository

    def get_vehicle_by_id(self, vehicle_id):
        return self.vehicle_repository.get_vehicle_by_id(vehicle_id)

    def get_available_vehicles(self):
        return self.vehicle_repository.get_available_vehicles()

    def add_vehicle(self, vehicle):
        return self.vehicle_repository.add_vehicle(vehicle)

    def update_vehicle(self, vehicle_id, new_vehicle_data):
        return self.vehicle_repository.update_vehicle(vehicle_id, new_vehicle_data)

    def remove_vehicle(self, vehicle_id):
        return self.vehicle_repository.remove_vehicle(vehicle_id)
'''
