from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from src.Domain.person import Person
from typing import Optional
from src.Storage.person_persistence import *
from src.Storage.DB import  *

class PersonMysql(PersonPersistence):
    SELECT = "SELECT * FROM Persons"
    SELECT_BY_ID = "SELECT * FROM Persons WHERE person_id=%s"
    SELECT_BY_EMAIL = "SELECT * FROM Persons WHERE email=%s"
    INSERTAR = "INSERT INTO Persons (first_name, last_name, email, phone) VALUES (%s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE Persons SET first_name =%s, last_name =%s, email =%s, phone =%s WHERE person_id =%s"
    ELIMINAR = "DELETE FROM Persons WHERE person_id =%s"

    def add(self, new_person: Person):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (new_person.name, new_person.last, new_person.email, new_person.phone)
            cursor.execute(PersonMysql.INSERTAR,query_values)
            conexion.commit()
            return f"Usuario {new_person.name} {new_person.last} agregado"
        except Exception as e:
            return f"Ocurrio un error al agregar el clinete: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def remove(self, new_person: Person):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (new_person.id,)
            print(query_values)
            cursor.execute(PersonMysql.ELIMINAR,query_values)
            conexion.commit()
            return f"Usuario {new_person.name} {new_person.last} eliminado"
        except Exception as e:
            return f"Ocurrio un error al agregar el clinete: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def update(self, person):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (person.name, person.last, person.email, person.phone, person.id)
            print(query_values)
            cursor.execute(PersonMysql.ACTUALIZAR, query_values)
            conexion.commit()
            return f"Usuario {person.name} {person.last} modificado"
        except Exception as e:
            return f"Ocurrio un error al agregar el clinete: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_all(self):
        lst_persons: list[Person] = []
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            cursor.execute(PersonMysql.SELECT)
            registros = cursor.fetchall()
            for registro in registros:
                person = Person(id=int(registro[0]),name=registro[1],last=registro[2], email=registro[3], phone=registro[4])
                lst_persons.append(person)
            return lst_persons
        except Exception as e:
            return f"Ocurrio un error al agregar el clinete: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_by_id(self, id: int) -> Optional[Person]:
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (id,)
            cursor.execute(PersonMysql.SELECT_BY_ID, query_values)
            registro = cursor.fetchone()
            person = Person(id=int(registro[0]), name=registro[1], last=registro[2], email=registro[3],
                            phone=registro[4])
            return person
        except Exception as e:
            return None
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_by_email(self, email: str) -> Optional[Person]:
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (email,)
            cursor.execute(PersonMysql.SELECT_BY_EMAIL, query_values)
            registro = cursor.fetchone()
            person = Person(id=int(registro[0]), name=registro[1], last=registro[2], email=registro[3],
                            phone=registro[4])
            return person
        except Exception as e:
            return None
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


