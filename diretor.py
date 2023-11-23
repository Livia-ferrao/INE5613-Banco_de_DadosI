from generic_table import GenericTable

class Diretor(GenericTable):
    def __init__(self):
        GenericTable.__init__(self)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS cinema.diretor (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255));"""  
        super().create_table(sql)

    def drop_table(self):
        super().drop_table("cinema.diretor")

    def insert(self, *args):
        sql = f'INSERT INTO cinema.diretor (nome) VALUES (%s);'
        super().insert(sql, *args)

    def delete(self, id):
        sql_exist = f'SELECT * FROM cinema.diretor WHERE id = {id}'
        if not self.query(sql_exist):
            print("Registro não encontrado para deletar")
        else:
            sql= f'DELETE FROM cinema.diretor WHERE id = {id}'
            super().delete(sql)

    def update(self, id, *args):
        sql_exist = f"SELECT * FROM cinema.diretor WHERE id = {id}"
        if not self.query(sql_exist):
            print("Registro não encontrado para atualizar")
        else:
            sql = f'UPDATE cinema.diretor SET nome = %s WHERE id = {id}'
            super().update(sql, *args)
    
    def get_by_id(self, id):
        sql = f"SELECT * FROM cinema.diretor WHERE id = {id}"
        return super().get_by_id(sql)

    def get_all(self):
        return super().get_all("cinema.diretor")
    
    def print(self):
        if self.get_all():
            print("--- DIRETORES ---")
            for i in self.get_all():
                print(f"{i[0]} - {i[1]}")
        else:
            print("Não existe nenhum diretor cadastrado")