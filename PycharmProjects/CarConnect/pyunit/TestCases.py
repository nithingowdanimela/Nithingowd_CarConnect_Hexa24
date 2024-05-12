import unittest
from dao.CustomerService import CustomerService
from dao.VehicleService import VehicleService
from dao.ReservationService import ReservationService
from dao.AdminService import AdminService


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer_service = CustomerService()
        self.vehicle_service = VehicleService()
        self.reservation_service = ReservationService()
        self.admin_service = AdminService()

    #Test1: Test customer authentication with invalid credentials.
    def test_1(self):
        result = self.customer_service.authenticate_customer_test('xyz', '456')
        self.assertEqual("Authentication failed-- Invalid username.", str(result))
        result = self.customer_service.authenticate_customer_test('nithin', '456')
        self.assertEqual("Authentication failed-- Invalid password.", str(result))
        result = self.customer_service.authenticate_customer_test('nithin', '12345')
        self.assertEqual("Authentication Successful!", str(result))

    #Test2: Test updating customer information.
    def test_2(self):
        print("Correct Details: ")
        result = self.customer_service.update_customer()
        self.assertEqual("Records Updated Successfully...", str(result))

    #Test3: Test adding a new vehicle.
    '''def test_3(self):
        print("Correct Details: ")
        result = self.vehicle_service.add_vehicle()
        self.assertEqual("Vehicle added successfully...", str(result))'''

    #Test4: Test updating vehicle details.
    '''def test_4(self):
        print("Correct Details: ")
        result = self.vehicle_service.update_vehicle()
        self.assertEqual("Vehicle Updated Successfully...", str(result))'''

    #Test5: Test getting a list of available vehicles.
    def test_5(self):
        result = self.vehicle_service.get_available_vehicles()
        self.assertEqual("True", str(result))

    #Test6: Test getting a list of all vehicles.
    def test_6(self):
        result = self.vehicle_service.get_available_vehicles()
        self.assertEqual("True", str(result))


if __name__ == '__main__':
    unittest.main()
