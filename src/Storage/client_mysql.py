from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor
from abc import ABC, abstractmethod
from typing import Optional
from src.Domain.client import Client
from src.Storage.client_persistence import ClientPersistence
from src.Storage.DB import  *


class ClientMysql(ClientPersistence):
    SELECT = "SELECT * FROM Clients"
    SELECT_BY_ID = "SELECT * FROM Clients WHERE client_id=%s"
    INSERTAR = "INSERT INTO Clients (person_id, tipo_membresia, ultimo_cobro, proximo_cobro, pendiente_pago) VALUES (%s, %s, %s, %s, %s)"
    ACTUALIZAR = "UPDATE Clients SET tipo_membresia =%s, ultimo_cobro =%s, proximo_cobro =%s, pendiente_pago =%s WHERE client_id =%s"
    ELIMINAR = "DELETE FROM Clients WHERE client_id =%s"

    def add(self, new_client: Client):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (new_client.person_id, new_client.membership_type, new_client.last_payment, new_client.next_payment, new_client.payment_pending)
            cursor.execute(ClientMysql.INSERTAR,query_values)
            conexion.commit()
            return f"Cliente PersonID:{new_client.person_id} TipoMembresia:{new_client.membership_type} agregado"
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def remove(self, new_client: Client):
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (new_client.id,)
            cursor.execute(ClientMysql.ELIMINAR,query_values)
            conexion.commit()
            return f"Cliente ClientID:{new_client.id} PersonID:{new_client.person_id} eliminado"
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def update(self, cliente: Client):
        ###"UPDATE Clients SET tipo_membresia =%s, ultimo_cobro =%s, proximo_cobro =%s, pendiente_pago =%s WHERE client_id =%s"
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (cliente.membership_type,cliente.last_payment,cliente.next_payment, cliente.next_payment, cliente.id)
            cursor.execute(ClientMysql.ACTUALIZAR, query_values)
            conexion.commit()
            return f"Cliente ClientID:{cliente.id} PersonID:{cliente.person_id} modificado"
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_all(self):
        lst_clients: list[Client] = []
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            cursor.execute(ClientMysql.SELECT)
            registros = cursor.fetchall()
            for registro in registros:
                client = Client(id=int(registro[0]),person_id=int(registro[1]),membership_type=registro[2]
                                , last_payment=registro[3], next_payment=registro[4], payment_pending=registro[5])
                lst_clients.append(client)
            return lst_clients
        except Exception as e:
            return f"Ocurrio un error al agregar el Cliente: {e}"
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    def get_by_id(self, id: int) -> Optional[Client]:
        conexion: MySQLConnection = None
        cursor: MySQLCursor = None
        try:
            conexion: MySQLConnection = Conexion.obtener_conexion()
            cursor: MySQLCursor = conexion.cursor()
            query_values = (id,)
            cursor.execute(ClientMysql.SELECT_BY_ID, query_values)
            registro = cursor.fetchone()
            person = Client(id=int(registro[0]),person_id=int(registro[1]),membership_type=registro[2]
                                , last_payment=registro[3], next_payment=registro[4], payment_pending=registro[5])
            return person
        except Exception as e:
            return None
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)