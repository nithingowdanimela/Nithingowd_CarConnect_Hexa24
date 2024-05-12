from abc import ABC, abstractmethod


class IReservationService(ABC):
    @abstractmethod
    def create_reservation(self):
        pass

    @abstractmethod
    def update_reservation(self):
        pass

    @abstractmethod
    def cancel_reservation(self):
        pass

    @abstractmethod
    def get_reservation_by_id(self):
        pass

    @abstractmethod
    def get_reservations_by_customer_id(self):
        pass

    @abstractmethod
    def select_reservation(self):
        pass
