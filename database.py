import mysql.connector
from config import Config

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        self.connection = mysql.connector.connect(
            host = Config.DB_HOST,
            user = Config.DB_USER,
            password = Config.DB_PASS,
            database = Config.DB_NAME
        )

    def get_connection(self):
        if not self.connection:
            self.connect()
        return self.connection
    
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None