from generic_table import GenericTable

class Exibicao(GenericTable):
    def __init__(self):
        GenericTable.__init__(self)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS cinema.exibicao (
                id_filme INT,
                id_sala INT,
                id_horario INT,
                data DATE,
                PRIMARY KEY (id_filme, id_sala, id_horario, data),
                FOREIGN KEY (id_filme) REFERENCES cinema.filme(id),
                FOREIGN KEY (id_sala) REFERENCES cinema.sala(id),
                FOREIGN KEY (id_horario) REFERENCES cinema.horario(id));"""  
        super().create_table(sql)

    def drop_table(self):
        super().drop_table("cinema.exibicao")

    def insert(self, *args):
        sql = f'INSERT INTO cinema.exibicao (id_filme, id_sala, id_horario, data) VALUES (%s, %s, %s, %s);'
        super().insert(sql, *args)

    def delete(self, id):
        sql_exist = f'SELECT * FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}'
        if not self.query(sql_exist):
            print("Registro não encontrado para deletar")
        else:
            sql= f'DELETE FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}'
            super().delete(sql)

    def update(self, id, *args):
        sql_exist = f"SELECT * FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}"
        if not self.query(sql_exist):
            print("Registro não encontrado para atualizar")
        else:
            sql = f'UPDATE cinema.exibicao SET data = %s WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}'
            super().update(sql, *args)
    
    def get_by_id(self, id):
        sql = f"SELECT * FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}"
        return super().get_by_id(sql)

    def get_all(self):
        return super().get_all("cinema.exibicao")
    
    def print(self, filme, sala, horario):
        if self.get_all():
            print("--- EXIBIÇÕES ---")
            for i in self.get_all():
                sql = f"""SELECT nome FROM cinema.filme WHERE id = {i[0]}"""
                sql_filme = filme.query(sql)
                sql = f"""SELECT nome FROM cinema.sala WHERE id = {i[1]}"""
                sql_sala = sala.query(sql)
                sql = f"""SELECT horario FROM cinema.horario WHERE id = {i[2]}"""
                sql_horario = horario.query(sql)
                print(f"{sql_filme[0][0]}, {sql_sala[0][0]}, {sql_horario[0][0]}, {i[3]}")
        else:
            print("Não existe nenhuma exibição cadastrada")