from generic_table import GenericTable

class Filme(GenericTable):
    def __init__(self):
        GenericTable.__init__(self)

    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS cinema.filme ( 
                id SERIAL PRIMARY KEY,
                nome VARCHAR(255),
                ano_lancamento INT,
                sinopse TEXT,
                id_diretor INT REFERENCES cinema.diretor(id),
                id_genero INT REFERENCES cinema.genero(id));""" 
        super().create_table(sql)

    def drop_table(self):
        super().drop_table("cinema.filme")

    def insert(self, *args):
        sql = f'INSERT INTO cinema.filme (nome, ano_lancamento, sinopse, id_diretor, id_genero) VALUES (%s, %s, %s, %s, %s);'
        super().insert(sql, *args)

    def delete(self, id):
        sql_exist = f'SELECT * FROM cinema.filme WHERE id = {id}'
        if not self.query(sql_exist):
            print("Registro não encontrado para deletar")
        else:
            sql= f'DELETE FROM cinema.filme WHERE id = {id}'
            super().delete(sql)

    def update(self, id, *args):
        sql_exist = f"SELECT * FROM cinema.filme WHERE id = {id}"
        if not self.query(sql_exist):
            print("Registro não encontrado para atualizar")
        else:
            sql = f'UPDATE cinema.filme SET nome = %s, ano_lancamento = %s, sinopse = %s, id_diretor = %s, id_genero = %s WHERE id = {id}'
            super().update(sql, *args)
    
    def get_by_id(self, id):
        sql = f"SELECT * FROM cinema.filme WHERE id = {id}"
        return super().get_by_id(sql)

    def get_all(self):
        return super().get_all("cinema.filme")
    
    def print(self, diretor, genero):
        if self.get_all():
            print(" --- FILMES --- ")
            for i in self.get_all():
                sql = f"""SELECT nome FROM cinema.diretor WHERE id = {i[4]}"""
                sql_diretor = diretor.query(sql)
                sql = f"""SELECT nome FROM cinema.genero WHERE id = {i[5]}"""
                sql_genero = genero.query(sql)
                print(f"{i[0]} - {i[1]}, {i[2]}, {i[3]}, {sql_diretor[0][0]}, {sql_genero[0][0]}")
        else:
            print("Não existe nenhum filme cadastrado")