from abc import ABC, abstractmethod


class IVehicleService(ABC):
    @abstractmethod
    def add_vehicle(self):
        pass

    @abstractmethod
    def update_vehicle(self):
        pass

    @abstractmethod
    def remove_vehicle(self):
        pass

    @abstractmethod
    def get_vehicle_by_id(self):
        pass

    @abstractmethod
    def get_available_vehicles(self):
        pass

    @abstractmethod
    def select_vehicle(self):
        pass
