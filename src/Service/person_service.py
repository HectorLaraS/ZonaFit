from src.Domain.client import Client
from src.Storage.person_persistence import PersonPersistence


class PersonService:
    def __init__(self, repo: PersonPersistence):
        self._repo = repo

    def add(self, new_person):
        return self._repo.add(new_person)

    def remove(self, person):
        return self._repo.remove(person)

    def update(self, person):
        return self._repo.update(person)

    def get_all(self):
        return self._repo.get_all()

    def get_by_id(self):
        return self._repo.get_by_id()

    def get_by_email(self, email):
        return self._repo.get_by_email(email)