from src.Domain.client import Client
from src.Storage.user_persistence import UserPersistence


class PersonService:
    def __init__(self, repo: UserPersistence):
        self._repo = repo

    def add(self, new_user):
        self._repo.add(new_user)

    def remove(self, user):
        self._repo.remove(user)

    def update(self, user):
        self._repo.update(user)

    def get_all(self):
        return self._repo.get_all()

    def get_by_id(self):
        return self._repo.get_all()