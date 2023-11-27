from generic_table import GenericTable
from tabulate import tabulate

class Indicacao_premiacao(GenericTable):
    def __init__(self):
        GenericTable.__init__(self)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS cinema.indicacao_premiacao (
                id_filme INT,
                id_premiacao INT,
                ganhou BOOL,
                PRIMARY KEY (id_filme, id_premiacao),
                FOREIGN KEY (id_filme) REFERENCES cinema.filme(id),
                FOREIGN KEY (id_premiacao) REFERENCES cinema.premiacao(id));"""  
        super().create_table(sql)

    def drop_table(self):
        super().drop_table("cinema.indicacao_premiacao")

    def insert(self, *args):
        sql = f'INSERT INTO cinema.indicacao_premiacao(id_filme, id_premiacao, ganhou) VALUES (%s, %s, %s);'
        super().insert(sql, *args)

    def delete(self, id):
        sql_exist = f'SELECT * FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}'
        if not self.query(sql_exist):
            print("Registro não encontrado para deletar")
        else:
            sql= f'DELETE FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}'
            super().delete(sql)

    def update(self, id, *args):
        sql_exist = f"SELECT * FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}"
        if not self.query(sql_exist):
            print("Registro não encontrado para atualizar")
        else:
            sql = f'UPDATE cinema.indicacao_premiacao SET ganhou = %s WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}'
            super().update(sql, *args)
    
    def get_by_id(self, id):
        sql = f"SELECT * FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}"
        return super().get_by_id(sql)

    def get_all(self):
        return super().get_all("cinema.indicacao_premiacao")
    
    def print(self, filme, sala):
        headers = ["Filme", "Premiação", "Ganhou?"]
        rows =[]
        if self.get_all():
            for i in self.get_all():
                sql = f"""SELECT nome FROM cinema.filme WHERE id = {i[0]}"""
                sql_filme = filme.query(sql)
                sql = f"""SELECT nome FROM cinema.premiacao WHERE id = {i[1]}"""
                sql_premiacao = sala.query(sql)

                if i[2] == True:
                    ganhou = "Ganhou"
                else:
                    ganhou = "Perdeu"
                rows.append([sql_filme[0][0], sql_premiacao[0][0], ganhou])

            print(tabulate(rows, headers=headers, tablefmt="fancy_grid", maxcolwidths=20))   
        else:
            print("Não existe nenhuma indicação cadastrada")