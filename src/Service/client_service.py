from src.Domain.client import Client
from src.Storage.client_persistence import ClientPersistence

class ClientService:
    def __init__(self, repo: ClientPersistence):
        self._repo  = repo

    def add(self, new_client):
        self._repo.add(new_client)

    def remove(self, client):
        self._repo.remove(client)

    def update(self, client):
        self._repo.update(client)

    def get_all(self):
        return self._repo.get_all()

    def get_by_id(self):
        return self._repo.get_all()
