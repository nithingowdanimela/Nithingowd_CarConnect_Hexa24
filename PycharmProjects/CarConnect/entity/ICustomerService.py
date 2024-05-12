from abc import ABC, abstractmethod


class ICustomerService(ABC):

    @abstractmethod
    def register_customer(self):
        pass

    @abstractmethod
    def update_customer(self):
        pass

    @abstractmethod
    def delete_customer(self):
        pass

    @abstractmethod
    def get_customer_by_id(self):
        pass

    @abstractmethod
    def get_customer_by_username(self):
        pass

    @abstractmethod
    def select_customers(self):
        pass
