import psycopg2 as db
from config import Config
from tabulate import tabulate

class Connection(Config):
    def __init__(self):
        Config.__init__(self)
        try:
            self.conn = db.connect(**self.config["postgres"])
            self.cur = self.conn.cursor()
        except Exception as e:
            print("Erro da conexão ", e)
            exit(1)

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, ext_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self.conn
    
    @property
    def cursor(self):
        return self.cur
    
    def commit(self):
        self.connection.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def create_schema(self, schema_name):
        try:
            sql = f'CREATE SCHEMA IF NOT EXISTS {schema_name};'
            self.execute(sql)
            self.commit()
            print(f"Esquema {schema_name} criado")
        except Exception as e:
            print(f"Erro ao criar o esquema {schema_name}", e)
