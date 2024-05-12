from abc import ABC, abstractmethod


class IAdminService(ABC):
    @abstractmethod
    def register_admin(self):
        pass

    @abstractmethod
    def update_admin(self):
        pass

    @abstractmethod
    def delete_admin(self):
        pass

    @abstractmethod
    def get_admin_by_id(self):
        pass

    @abstractmethod
    def get_admin_by_username(self):
        pass

    @abstractmethod
    def select_admin(self):
        pass
