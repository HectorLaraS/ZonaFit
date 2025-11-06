from abc import ABC, abstractmethod
from src.Domain.person import Person

class PersonPersistence:

    @abstractmethod
    def add(self, new_person):
        pass

    @abstractmethod
    def remove(self, person):
        pass

    @abstractmethod
    def update(self, person):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self):
        pass
