# mysql.py

import mysql.connector
from mysql.connector.pooling import MySQLConnectionPool

from app.utils.config import Config
from app.utils.logger import get_logger

logger = get_logger(__name__)


class Database:

    _pool = None

    @classmethod
    def initialize(cls):

        if cls._pool is None:

            logger.info("Creating MySQL Connection Pool")

            cls._pool = MySQLConnectionPool(
                pool_name="department_pool",
                pool_size=10,
                host=Config.MYSQL_HOST,
                port=Config.MYSQL_PORT,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DATABASE,
                autocommit=False
            )

            logger.info("MySQL Pool Created")

    @classmethod
    def connection(cls):

        if cls._pool is None:
            cls.initialize()

        return cls._pool.get_connection()

    @classmethod
    def get_transaction(cls):

        conn = cls.connection()

        cursor = conn.cursor(dictionary=True)

        return conn, cursor
# ----------------------------
# STEP 4 STARTS HERE
# ----------------------------

class DatabaseHelper:

    @staticmethod
    def fetch_one(query, params=None):

        conn = Database.connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            return cursor.fetchone()

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def fetch_all(query, params=None):

        conn = Database.connection()
        cursor = conn.cursor(dictionary=True)

        try:
            cursor.execute(query, params)
            return cursor.fetchall()

        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def execute(query, params=None):

        conn = Database.connection()
        cursor = conn.cursor()

        try:
            cursor.execute(query, params)
            conn.commit()

            return cursor.lastrowid

        except Exception:
            conn.rollback()
            raise

        finally:
            cursor.close()
            conn.close()