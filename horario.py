from generic_table import GenericTable

class Horario(GenericTable):
    def __init__(self):
        GenericTable.__init__(self)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS cinema.horario (
                id SERIAL PRIMARY KEY,
                time TIME);"""  
        super().create_table(sql)

    def drop_table(self):
        super().drop_table("cinema.horario")

    def insert(self, *args):
        sql = f'INSERT INTO cinema.horario (time) VALUES (%s);'
        super().insert(sql, *args)

    def delete(self, id):
        sql_exist = f'SELECT * FROM cinema.horario WHERE id = {id}'
        if not self.query(sql_exist):
            print("Registro não encontrado para deletar")
        else:
            sql= f'DELETE FROM cinema.horario WHERE id = {id}'
            super().delete(sql)

    def update(self, id, *args):
        sql_exist = f"SELECT * FROM cinema.horario WHERE id = {id}"
        if not self.query(sql_exist):
            print("Registro não encontrado para atualizar")
        else:
            sql = f'UPDATE cinema.horario SET time = %s WHERE id = {id}'
            super().update(sql, *args)
    
    def get_by_id(self, id):
        sql = f"SELECT * FROM cinema.horario WHERE id = {id}"
        return super().get_by_id(sql)

    def get_all(self):
        return super().get_all("cinema.horario")
    
    def print(self):
        if self.get_all():
                print("--- HORÁRIOS ---")
                for i in self.get_all():
                    print(f"{i[0]} - {i[1]}")
        else:
            print("Não existe nenhum horário cadastrado")