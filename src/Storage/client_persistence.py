from abc import ABC, abstractmethod
from typing import Optional
from src.Domain.client import Client

class ClientPersistence:

    @abstractmethod
    def add(self, new_client):
        pass

    @abstractmethod
    def remove(self, client):
        pass

    @abstractmethod
    def update(self, client):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, id) -> Optional["Person"]:
        pass

    @abstractmethod
    def get_by_user_id(self, id) -> Optional["Person"]:
        pass
