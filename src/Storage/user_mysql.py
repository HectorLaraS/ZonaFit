from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from abc import ABC, abstractmethod
from typing import Optional
from src.Storage.client_persistence import ClientPersistence
from src.Domain.user import User
from src.Storage.user_persistence import UserPersistence
from src.Storage.DB import  *


class UserMysql(UserPersistence):
    SELECT = "SELECT * FROM Users"
    SELECT_BY_ID = "SELECT * FROM Users WHERE user_id=%s"
    SELECT_BY_USERNAME = "SELECT * FROM Users WHERE username=%s"
    INSERTAR = "INSERT INTO Users (username,password_hash,person_id) VALUES (%s, %s, %s)"
    ACTUALIZAR = "UPDATE Users SET username =%s, password_hash =%s WHERE user_id =%s"
    ELIMINAR = "DELETE FROM Users WHERE user_id =%s"

    def add(self, user: User):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (user.username, user.password, user.person_id)
            cursor.execute(UserMysql.INSERTAR,query_values)
            conexion.commit()
            return f"User:{user} agregado"
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def remove(self, user: User):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (user.id,)
            cursor.execute(UserMysql.ELIMINAR,query_values)
            conexion.commit()
            return f"User:{user} eliminado"
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def update(self, user: User):
        ###"UPDATE Users SET username =%s, password_hash =%s WHERE user_id =%s"
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (user.username, user.password, user.id)
            cursor.execute(UserMysql.ACTUALIZAR, query_values)
            conexion.commit()
            return f"User:{user} modificado"
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_all(self):
        lst_users: list[User] = []
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            cursor.execute(UserMysql.SELECT)
            registros = cursor.fetchall()
            for registro in registros:
                user = User(id=int(registro[0]),username=registro[1],password=registro[2],person_id=int(registro[3]))
                lst_users.append(user)
            return lst_users
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_by_id(self, id: int) -> Optional[User]:
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (id,)
            cursor.execute(UserMysql.SELECT_BY_ID, query_values)
            registro = cursor.fetchone()
            person = User(id=int(registro[0]),username=registro[1],password=registro[2],person_id=int(registro[3]))
            return person
        except Exception as e:
            return None
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_by_user(self, username: str) -> Optional[User]:
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (username,)
            cursor.execute(UserMysql.SELECT_BY_USERNAME, query_values)
            registro = cursor.fetchone()
            person = User(id=int(registro[0]),username=registro[1],password=registro[2],person_id=int(registro[3]))
            return person
        except Exception as e:
            return None
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)