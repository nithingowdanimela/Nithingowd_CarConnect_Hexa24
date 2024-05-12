from dao.AdminService import AdminService
from dao.CustomerService import CustomerService
from dao.ReservationService import ReservationService
from dao.VehicleService import VehicleService
from exception.InvalidInputException import InvalidInputException


class Main:
    def __init__(self):
        self.loop = None

    def main(self):
        self.loop = True
        while self.loop:
            try:
                customerservice = CustomerService()
                vehicleservice = VehicleService()
                reservationservice = ReservationService()
                adminservice = AdminService()
                print("\nWelcome to CarConnect!!!")
                print("Select option to use functionalities: ")
                print("1.Customer\n2.Vehicle\n3.Reservation\n4.Admin\n5.Exit")
                choice = int(input("Enter your choice: "))
                if str(choice) in "12345":
                    if choice == 1:
                        while True:
                            print('''1.Add Customer\n2.Update Customer\n3.Delete Customer\n4.Get Customer details by ID
5.Get Customer details by Username\n6.View All Customers\n7.Exit
                            ''')
                            choice_1 = int(input("Enter your Choice: "))
                            if str(choice_1) in "1234567":
                                if choice_1 == 1:
                                    customerservice.register_customer()
                                elif choice_1 == 2:
                                    customerservice.update_customer()
                                elif choice_1 == 3:
                                    customerservice.delete_customer()
                                elif choice_1 == 4:
                                    customerservice.get_customer_by_id()
                                elif choice_1 == 5:
                                    customerservice.get_customer_by_username()
                                elif choice_1 == 6:
                                    customerservice.select_customers()
                                else:
                                    break
                            else:
                                raise InvalidInputException("Input should be between 1 and 7")
                    elif choice == 2:
                        while True:
                            print('''1.Add Vehicle\n2.Update Vehicle\n3.Remove Vehicle\n4.Get Vehicle details by ID
5.Get Available Vehicles\n6.Get All Vehicles\n7.Exit
                            ''')
                            choice_2 = int(input("Enter your Choice: "))
                            if str(choice_2) in "1234567":
                                if choice_2 == 1:
                                    vehicleservice.add_vehicle()
                                elif choice_2 == 2:
                                    vehicleservice.update_vehicle()
                                elif choice_2 == 3:
                                    vehicleservice.remove_vehicle()
                                elif choice_2 == 4:
                                    vehicleservice.get_vehicle_by_id()
                                elif choice_2 == 5:
                                    vehicleservice.get_available_vehicles()
                                elif choice_2 == 6:
                                    vehicleservice.select_vehicle()
                                else:
                                    break
                            else:
                                raise InvalidInputException("Input should be between 1 and 7")
                    elif choice == 3:
                        while True:
                            print('''1.Create Reservation\n2.Update Reservation\n3.Cancel Reservation\n4.Get Reservation by ID
5.Get Reservations by CustomerId\n6.Get All Reservations\n7.Exit
                            ''')
                            choice_3 = int(input("Enter your Choice: "))
                            if str(choice_3) in "1234567":
                                if choice_3 == 1:
                                    reservationservice.create_reservation()
                                elif choice_3 == 2:
                                    reservationservice.update_reservation()
                                elif choice_3 == 3:
                                    reservationservice.cancel_reservation()
                                elif choice_3 == 4:
                                    reservationservice.get_reservation_by_id()
                                elif choice_3 == 5:
                                    reservationservice.get_reservations_by_customer_id()
                                elif choice_3 == 6:
                                    reservationservice.select_reservation()
                                else:
                                    break
                            else:
                                raise InvalidInputException("Input should be between 1 and 7")
                    elif choice == 4:
                        while True:
                            print('''1.Register Admin\n2.Update Admin\n3.Delete Admin\n4.Get Admin By Id\n5.Get Admin By Username
6.Get All Admins\n7.Exit
                            ''')
                            choice_4 = int(input("Enter your Choice: "))
                            if str(choice_4) in "1234567":
                                if choice_4 == 1:
                                    adminservice.register_admin()
                                elif choice_4 == 2:
                                    adminservice.update_admin()
                                elif choice_4 == 3:
                                    adminservice.delete_admin()
                                elif choice_4 == 4:
                                    adminservice.get_admin_by_id()
                                elif choice_4 == 5:
                                    adminservice.get_admin_by_username()
                                elif choice_4 == 6:
                                    adminservice.select_admin()
                                else:
                                    break
                            else:
                                raise InvalidInputException("Input should be between 1 and 7")
                    else:
                        exit()
                else:
                    raise InvalidInputException("Input should be between 1 and 5")
            except InvalidInputException as e:
                print(f"Invalid input: {e}")
            except Exception as e:
                print(f"An error occurred: {e}")
            finally:
                print("Thank You for reaching CarConnect")


obj = Main()
obj.main()
