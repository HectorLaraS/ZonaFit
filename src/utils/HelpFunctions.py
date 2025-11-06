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

def bootstrap_service_user():
    persistencia = UserMysql()
    service = UserService(persistencia)
    return service

def bootstrap_service_client():
    persistencia = ClientMysql()
    service = ClientService(persistencia)
    return service

def bootstrap_service_person():
    persistencia = PersonMysql()
    service = PersonService(persistencia)
    return service