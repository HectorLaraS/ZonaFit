from abc import ABC, abstractmethod
from src.Domain.user import User

class UserPersistence:

    @abstractmethod
    def add(self, new_user):
        pass

    @abstractmethod
    def remove(self, user):
        pass

    @abstractmethod
    def update(self, user):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id):
        pass

    @abstractmethod
    def get_by_user(self, username):
        pass
