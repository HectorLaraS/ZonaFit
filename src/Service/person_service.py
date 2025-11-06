from src.Domain.client import Client
from src.Storage.person_persistence import PersonPersistence


class PersonService:
    def __init__(self, repo: PersonPersistence):
        self._repo = repo

    def add(self, new_person):
        self._repo.add(new_person)

    def remove(self, person):
        self._repo.remove(person)

    def update(self, person):
        self._repo.update(person)

    def get_all(self):
        return self._repo.get_all()

    def get_by_id(self):
        return self._repo.get_all()