from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from abc import ABC, abstractmethod
from typing import Optional
from src.utils.password import *
from src.Domain.client import *
from src.Domain.person import *
from src.Domain.user import *
from src.Storage.DB import *
from src.Storage.user_persistence import *
from src.Storage.client_persistence import *
from src.Storage.person_persistence import *
from src.Storage.user_mysql import *
from src.Storage.client_mysql import *
from src.Storage.person_mysql import *
from src.Service.user_service import *
from src.Service.client_service import *
from src.Service.person_service import *
from src.utils.HelpFunctions import *

class LoginController:
    def __init__(self):
        pass

    def authenticate(self, username: str, password: str) -> bool:
        output = False
        service = bootstrap_service_user()
        user = service.get_by_user(username)
        print()
        if username == user.username and hash_password_md5(password) == user.password:
            output = True
        return output


if __name__ == "__main__":
    login_controller = LoginController()
    print(login_controller.authenticate("hlaras","Boston23!.!"))

