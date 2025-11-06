import os
from mysql.connector import  pooling
from mysql.connector import Error
from dotenv import load_dotenv
load_dotenv()

class Conexion:
    DATABASE = os.getenv("DB_NAME")
    USERNAME = os.getenv("DB_USER")
    PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")
    HOST = os.getenv("DB_HOST")
    POOL_ZISE = 5
    POOL_NAME = "zonafit_pool"
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_ZISE,
                    host = cls.HOST,
                    port= cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al obtener pool: {e}")
        else:
            return cls.pool

    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()