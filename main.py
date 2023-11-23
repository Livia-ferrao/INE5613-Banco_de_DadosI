from diretor import Diretor
from genero import Genero
from exibicao import Exibicao
from filme import Filme
from horario import Horario
from premiacao import Premiacao
from sala import Sala
from indicacao_premiacao import Indicacao_premiacao
from connection import Connection

# class Config:
#     def __init__(self):
#         self.config = {
#             "postgres": {
#                 "user":"postgres",
#                 "password": "postgres",
#                 "host": "127.0.0.1",
#                 "port": "5432",
#             }
#         }

# class Connection(Config):
#     def __init__(self):
#         Config.__init__(self)
#         try:
#             self.conn = db.connect(**self.config["postgres"])
#             self.cur = self.conn.cursor()
#         except Exception as e:
#             print("Erro da conexão ", e)
#             exit(1)

#     def __enter__(self):
#         return self
    
#     def __exit__(self, exc_type, exc_val, ext_tb):
#         self.commit()
#         self.connection.close()

#     @property
#     def connection(self):
#         return self.conn
    
#     @property
#     def cursor(self):
#         return self.cur
    
#     def commit(self):
#         self.connection.commit()

#     def fetchall(self):
#         return self.cursor.fetchall()
    
#     def execute(self, sql, params=None):
#         self.cursor.execute(sql, params or ())

#     def query(self, sql, params=None):
#         self.cursor.execute(sql, params or ())
#         return self.fetchall()

#     def create_schema(self, schema_name):
#         try:
#             sql = f'CREATE SCHEMA IF NOT EXISTS {schema_name};'
#             self.execute(sql)
#             self.commit()
#             print(f"Esquema {schema_name} criado")
#         except Exception as e:
#             print(f"Erro ao criar o esquema {schema_name}", e)

# class GenericTable(Connection):
#     def __init__(self):
#         Connection.__init__(self)
    
#     def create_table(self, sql):
#         try:
#             self.execute(sql)
#             self.commit()
#             print("Tabela criada")
#         except Exception as e:
#             print("Erro ao criar a tabela ", e)

#     def drop_table(self, table_name):
#         try:
#             sql = f"""drop table {table_name} CASCADE;"""
#             self.execute(sql)
#             self.commit()
#             print("Tabela deletada")
#         except Exception as e:
#             print("Erro ao deletar a tabela ", e)

#     def insert(self, sql, *args):
#         try:
#             self.execute(sql, args)
#             self.commit()
#             print("Registro inserido")
#         except Exception as e:
#             print("Erro ao inserir ", e)

#     def delete(self, sql):
#         try:
#             self.execute(sql)
#             self.commit()
#             print("Registro deletado")
#         except Exception as e:
#             print("Erro ao deletar ", e)
    
#     def update(self, sql, *args):
#         try:
#             self.execute(sql, args)
#             self.commit()
#             print("Registro atualizado")
#         except Exception as e:
#             print("Erro ao atualizar ", e)

#     def get_by_id(self, sql):
#         data = self.query(sql)
#         if data:
#             return data
#         else:
#             print("Registro não encontrado")
#             return 

#     def get_all(self, table_name):
#         sql = f"SELECT * FROM {table_name}"
#         data = self.query(sql)
#         if data:
#             return data
#         else:
#             print("Registros não encontrados")
#             return 
    
# class Diretor(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.diretor (
#                 id SERIAL PRIMARY KEY,
#                 nome VARCHAR(255));"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.diretor")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.diretor (nome) VALUES (%s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.diretor WHERE id = {id}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.diretor WHERE id = {id}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.diretor WHERE id = {id}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.diretor SET nome = %s WHERE id = {id}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.diretor WHERE id = {id}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.diretor")
    
#     def print(self):
#         if self.get_all():
#             print("--- DIRETORES ---")
#             for i in self.get_all():
#                 print(f"{i[0]} - {i[1]}")
#         else:
#             print("Não existe nenhum diretor cadastrado")


# class Genero(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.genero (
#                 id SERIAL PRIMARY KEY,
#                 nome VARCHAR(255));"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.genero")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.genero (nome) VALUES (%s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.genero WHERE id = {id}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.genero WHERE id = {id}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.genero WHERE id = {id}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.genero SET nome = %s WHERE id = {id}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.genero WHERE id = {id}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.genero")
    
#     def print(self):
#         if self.get_all():
#             print("--- GÊNEROS ---")
#             for i in self.get_all():
#                 print(f"{i[0]} - {i[1]}")
#         else:
#             print("Não existe nenhum gênero cadastrado")


# class Filme(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.filme (
#                 id SERIAL PRIMARY KEY,
#                 nome VARCHAR(255),
#                 ano_lancamento INT,
#                 sinopse TEXT,
#                 id_diretor INT REFERENCES cinema.diretor(id),
#                 id_genero INT REFERENCES cinema.genero(id));""" 
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.filme")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.filme (nome, ano_lancamento, sinopse, id_diretor, id_genero) VALUES (%s, %s, %s, %s, %s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.filme WHERE id = {id}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.filme WHERE id = {id}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.filme WHERE id = {id}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.filme SET nome = %s, ano_lancamento = %s, sinopse = %s, id_diretor = %s, id_genero = %s WHERE id = {id}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.filme WHERE id = {id}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.filme")
    
#     def print(self):
#         if self.get_all():
#             print(" --- FILMES --- ")
#             for i in self.get_all():
#                 sql = f"""SELECT nome FROM cinema.diretor WHERE id = {i[4]}"""
#                 sql_diretor = diretor.query(sql)
#                 sql = f"""SELECT nome FROM cinema.genero WHERE id = {i[5]}"""
#                 sql_genero = genero.query(sql)
#                 print(f"{i[0]} - {i[1]}, {i[2]}, {i[3]}, {sql_diretor[0][0]}, {sql_genero[0][0]}")
#         else:
#             print("Não existe nenhum filme cadastrado")


# class Premiacao(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.premiacao (
#                 id SERIAL PRIMARY KEY,
#                 nome VARCHAR(255),
#                 ano INT);"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.premiacao")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.premiacao (nome, ano) VALUES (%s, %s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.premiacao WHERE id = {id}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.premiacao WHERE id = {id}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.premiacao WHERE id = {id}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.premiacao SET nome = %s, ano = %s WHERE id = {id}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.premiacao WHERE id = {id}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.premiacao")
    
#     def print(self):
#         if self.get_all():
#             print("--- PREMIAÇÕES ---")
#             for i in self.get_all():
#                 print(f"{i[0]} - {i[1]}, {i[2]}")
#         else:
#             print("Não existe nenhuma premiação cadastrada")


# class Indicacao_premiacao(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.indicacao_premiacao (
#                 id_filme INT,
#                 id_premiacao INT,
#                 ganhou BOOL,
#                 PRIMARY KEY (id_filme, id_premiacao),
#                 FOREIGN KEY (id_filme) REFERENCES cinema.filme(id),
#                 FOREIGN KEY (id_premiacao) REFERENCES cinema.premiacao(id));"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.indicacao_premiacao")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.indicacao_premiacao(id_filme, id_premiacao, ganhou) VALUES (%s, %s, %s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.indicacao_premiacao SET ganhou = %s WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.indicacao_premiacao WHERE id_filme = {id[0]} AND id_premiacao = {id[1]}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.indicacao_premiacao")
    
#     def print(self):
#         if self.get_all():
#             print("--- INDICAÇÕES A PREMIAÇÕES ---")
#             for i in self.get_all():
#                 sql = f"""SELECT nome FROM cinema.filme WHERE id = {i[0]}"""
#                 sql_filme = filme.query(sql)
#                 sql = f"""SELECT nome FROM cinema.premiacao WHERE id = {i[1]}"""
#                 sql_premiacao = sala.query(sql)
#                 if i[2] == True:
#                     print(f"{sql_filme[0][0]}, {sql_premiacao[0][0]}, Ganhou")
#                 else:
#                     print(f"{sql_filme[0][0]}, {sql_premiacao[0][0]}, Perdeu")
#         else:
#             print("Não existe nenhuma indicação cadastrada")


# class Sala(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.sala (
#                 id SERIAL PRIMARY KEY,
#                 nome VARCHAR(255),
#                 capacidade INT);"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.sala")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.sala (nome, capacidade) VALUES (%s, %s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.sala WHERE id = {id}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.sala WHERE id = {id}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.sala WHERE id = {id}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.sala SET nome = %s, capacidade = %s WHERE id = {id}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.sala WHERE id = {id}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.sala")
    
#     def print(self):
#         if self.get_all():
#             print("--- SALAS ---")
#             for i in self.get_all():
#                 print(f"{i[0]} - {i[1]}, {i[2]}")
#         else:
#             print("Não existe nenhuma sala cadastrada")


# class Horario(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.horario (
#                 id SERIAL PRIMARY KEY,
#                 time TIME);"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.horario")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.horario (time) VALUES (%s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.horario WHERE id = {id}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.horario WHERE id = {id}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.horario WHERE id = {id}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.horario SET time = %s WHERE id = {id}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.horario WHERE id = {id}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.horario")
    
#     def print(self):
#         if self.get_all():
#                 print("--- HORÁRIOS ---")
#                 for i in self.get_all():
#                     print(f"{i[0]} - {i[1]}")
#         else:
#             print("Não existe nenhum horário cadastrado")


# class Exibicao(GenericTable):
#     def __init__(self):
#         GenericTable.__init__(self)

#     def create_table(self):
#         sql = """CREATE TABLE IF NOT EXISTS cinema.exibicao (
#                 id_filme INT,
#                 id_sala INT,
#                 id_horario INT,
#                 data DATE,
#                 PRIMARY KEY (id_filme, id_sala, id_horario, data),
#                 FOREIGN KEY (id_filme) REFERENCES cinema.filme(id),
#                 FOREIGN KEY (id_sala) REFERENCES cinema.sala(id),
#                 FOREIGN KEY (id_horario) REFERENCES cinema.horario(id));"""  
#         super().create_table(sql)

#     def drop_table(self):
#         super().drop_table("cinema.exibicao")

#     def insert(self, *args):
#         sql = f'INSERT INTO cinema.exibicao (id_filme, id_sala, id_horario, data) VALUES (%s, %s, %s, %s);'
#         super().insert(sql, *args)

#     def delete(self, id):
#         sql_exist = f'SELECT * FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}'
#         if not self.query(sql_exist):
#             print("Registro não encontrado para deletar")
#         else:
#             sql= f'DELETE FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}'
#             super().delete(sql)

#     def update(self, id, *args):
#         sql_exist = f"SELECT * FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}"
#         if not self.query(sql_exist):
#             print("Registro não encontrado para atualizar")
#         else:
#             sql = f'UPDATE cinema.exibicao SET data = %s WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}'
#             super().update(sql, *args)
    
#     def get_by_id(self, id):
#         sql = f"SELECT * FROM cinema.exibicao WHERE id_filme = {id[0]} and id_sala = {id[1]} and id_horario = {id[2]}"
#         return super().get_by_id(sql)

#     def get_all(self):
#         return super().get_all("cinema.exibicao")
    
#     def print(self):
#         if self.get_all():
#             print("--- EXIBIÇÕES ---")
#             for i in self.get_all():
#                 sql = f"""SELECT nome FROM cinema.filme WHERE id = {i[0]}"""
#                 sql_filme = filme.query(sql)
#                 sql = f"""SELECT nome FROM cinema.sala WHERE id = {i[1]}"""
#                 sql_sala = sala.query(sql)
#                 sql = f"""SELECT horario FROM cinema.horario WHERE id = {i[2]}"""
#                 sql_horario = horario.query(sql)
#                 print(f"{sql_filme[0][0]}, {sql_sala[0][0]}, {sql_horario[0][0]}, {i[3]}")
#         else:
#             print("Não existe nenhuma exibição cadastrada")
    

if __name__ == "__main__":
    connection = Connection()
    # connection.create_schema("cinema")

    diretor = Diretor()
    diretor.drop_table()
    diretor.create_table()
    diretor.insert("João")
    diretor.insert("Maria")
    diretor.insert("Ana")
    # print("DIRETORES: ")
    # diretor.get_all()
    # # diretor.delete(2)
    # # diretor.update(4, "Pedro")
    # # diretor.get_by_id(5)

    genero = Genero()
    genero.drop_table()
    genero.create_table()
    genero.insert("Terror")
    genero.insert("Ação")
    genero.insert("Romance")
    # print("GÊNEROS: ")
    # genero.get_all()

    filme = Filme()
    filme.drop_table()
    filme.create_table()
    filme.insert("Rio", "2010", "Filme brasileiro", 3, 1)
    filme.insert("Ave", "2012", "Filme europeu", 2, 2)
    # # filme.update(1, "Rio", "2010", "Filme brasileiro", 3, 1)
    # print("FILMES: ")
    # filme.get_all()

    premiacao = Premiacao()
    premiacao.drop_table()
    premiacao.create_table()
    premiacao.insert("Oscar2012", "2012")
    premiacao.insert("Globo de ouro", "2015")
    premiacao.insert("Critics Choice Awards", "2018")
    premiacao.insert("Producers Guild Awards", "2020")
    premiacao.insert("Screen Actors Guild Awards", "2017")
    premiacao.insert("Writers Guild Awards", "2019")
    premiacao.insert("Directors Guild Awards", "2014")
    # print("PREMIAÇÃO")
    # premiacao.get_all()

    indicacao_premiacao = Indicacao_premiacao()
    indicacao_premiacao.drop_table()
    indicacao_premiacao.create_table()
    # # id_filme, id_premiacao, ganhou
    indicacao_premiacao.insert(1, 1, False)
    indicacao_premiacao.insert(1, 2, False)
    # # filme_premio.delete((1, 2))
    # # filme_premio.update((1,1), True)
    # print("FILME TEM REGISTRO? ")
    # filme_premio.get_all()

    sala = Sala()
    sala.drop_table()
    sala.create_table()
    sala.insert("Sala1", 50)
    sala.insert("Sala2", 60)
    # # sala.delete(2)
    # print("SALA: ")
    # sala.get_all()

    horario = Horario()
    horario.drop_table()
    horario.create_table()
    horario.insert("12:34:56")
    horario.insert("12:50:10")
    # print("HORÁRIOS: ")
    # horario.get_all()

    exibicao = Exibicao()
    exibicao.drop_table()
    exibicao.create_table()
    # # id_filme, id_sala, id_horario
    exibicao.insert(1, 1, 1, '2023-11-22')
    # print("EXIBIÇÕES: ")
    # exibicao.get_all()

    # data = filme.query("SELECT filme.nome, genero.nome, diretor.nome FROM cinema.filme JOIN cinema.genero ON filme.id_genero = genero.id JOIN cinema.diretor ON filme.id_diretor = diretor.id;")
    # print(data)
    

    while True:
        print("\n-------- MENU CINEMA --------")
        print("1 - Diretor")
        print("2 - Gênero")
        print("3 - Filme")
        print("4 - Premiação")
        print("5 - Indicação a premiação")
        print("6 - Sala")
        print("7 - Horário")
        print("8 - Exibição")
        print("9 - Consultas SQL")
        print("10 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            while True:
                print("\n-------- MENU DIRETOR --------")
                print("1 - Inserir Diretor")
                print("2 - Deletar Diretor")
                print("3 - Atualizar Diretor")
                print("4 - Buscar Diretor por ID")
                print("5 - Listar Todos os Diretores")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_diretor = input("Digite o nome do diretor: ")
                    diretor.insert(nome_diretor)

                elif escolha == "2":
                    if(diretor.get_all()):
                        print()
                        diretor.print()    
                        print()
                        id_diretor = input("Digite o ID do diretor a ser deletado: ")
                        diretor.delete(id_diretor)

                elif escolha == "3":
                    if(diretor.get_all()):
                        print()
                        diretor.print()
                        print()
                        id_diretor = input("Digite o ID do diretor a ser atualizado: ")
                        nome_diretor = input("Digite o novo nome do diretor: ")
                        diretor.update(id_diretor, nome_diretor)

                elif escolha == "4":
                    id_diretor = input("Digite o ID do diretor a ser buscado: ")
                    d = diretor.get_by_id(id_diretor)
                    if d:
                        print()
                        print(f"{d[0][0]} - {d[0][1]}")
    
                elif escolha == "5":
                    if(diretor.get_all()):
                        print()
                        diretor.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "2":
            while True:
                print("\n-------- MENU GÊNERO --------")
                print("1 - Inserir Gênero")
                print("2 - Deletar Gênero")
                print("3 - Atualizar Gênero")
                print("4 - Buscar Gênero por ID")
                print("5 - Listar Todos os Gêneros")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_genero = input("Digite o nome do gênero: ")
                    genero.insert(nome_genero)

                elif escolha == "2":
                    if(genero.get_all()):
                        print()
                        genero.print()
                        print()     
                        id_genero = input("Digite o ID do gênero a ser deletado: ")
                        genero.delete(id_genero)

                elif escolha == "3":
                    if(genero.get_all()):
                        print()
                        genero.print()
                        print()
                        id_genero = input("Digite o ID do gênero a ser atualizado: ")
                        nome_genero = input("Digite o novo nome do gênero: ")
                        genero.update(id_genero, nome_genero)

                elif escolha == "4":
                    id_genero = input("Digite o ID do gênero a ser buscado: ")
                    g = genero.get_by_id(id_genero)
                    if g:
                        print()
                        print(f"{g[0][0]} - {g[0][1]}")
    
    
                elif escolha == "5":
                    if(genero.get_all()):
                        print()
                        genero.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "3":
            while True:
                print("\n-------- MENU FILME --------")
                print("1 - Inserir Filme")
                print("2 - Deletar Filme")
                print("3 - Atualizar Filme")
                print("4 - Buscar Filme por ID")
                print("5 - Listar Todos os Filmes")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    if diretor.get_all():
                        if genero.get_all():
                            nome_filme = input("Digite o nome do filme: ")
                            ano_lancamento = input("Digite o ano de lançamento do filme: ")
                            sinopse = input("Digite a sinopse do filme: ")
                            print()
                            diretor.print()
                            print()
                            id_diretor = input("Digite o ID do diretor: ")
                            print()
                            genero.print()
                            print()
                            id_genero = input("Digite o ID do gênero: ")
                            filme.insert(nome_filme, ano_lancamento, sinopse, int(id_diretor), int(id_genero))
                        else:
                            print("Não existem gêneros cadastrados para inserir o filme")
                    else:
                        print("Não existem diretores cadastrados para inserir o filme")

                elif escolha == "2":
                    if(filme.get_all()):
                        print()
                        filme.print(diretor, genero)
                        print()
                        id_filme = input("Digite o ID do filme a ser deletado: ")
                        filme.delete(id_filme)

                elif escolha == "3":
                    if(filme.get_all()):
                        print()
                        filme.print(diretor, genero)
                        print()
                        id_filme = input("Digite ID do filme a ser atualizado: ")
                        nome_filme = input("Digite o nome do filme: ")
                        ano_lancamento = input("Digite o ano de lançamento do filme: ")
                        sinopse = input("Digite a sinopse do filme: ")
                        print()
                        diretor.print()
                        print()
                        id_diretor = input("Digite o ID do diretor: ")
                        print()
                        genero.print()
                        print()
                        id_genero = input("Digite o ID do gênero: ")
                        filme.update(id_filme, nome_filme, ano_lancamento, sinopse, id_diretor, id_genero)

                elif escolha == "4":
                    id_filme = input("Digite o ID do filme a ser buscado: ")
                    f = filme.get_by_id(id_filme)
                    if f:
                        print(f[0])
                        sql = f"""SELECT nome FROM cinema.diretor WHERE id = {f[0][4]}"""
                        sql_diretor = diretor.query(sql)
                        sql = f"""SELECT nome FROM cinema.genero WHERE id = {f[0][5]}"""
                        sql_genero = genero.query(sql)
                        print()
                        print(f"{f[0][0]} - {f[0][1]}, {f[0][2]}, {f[0][3]}, {sql_diretor[0][0]}, {sql_genero[0][0]}")
    
                elif escolha == "5":
                    if(filme.get_all()):
                        print()
                        filme.print(diretor, genero)
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "4":
            while True:
                print("\n-------- MENU PREMIAÇÃO --------")
                print("1 - Inserir Premiação")
                print("2 - Deletar Premiação")
                print("3 - Atualizar Premiação")
                print("4 - Buscar Premiação por ID")
                print("5 - Listar Todas as Premiaçãos")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_premiacao = input("Digite o nome da premiação: ")
                    ano_premiacao = input("Digite o ano da premiação: ")
                    premiacao.insert(nome_premiacao, ano_premiacao)

                elif escolha == "2":
                    if(premiacao.get_all()):
                        print()
                        premiacao.print()
                        print()
                        id_prem = input("Digite o ID da premiação a ser deletada: ")
                        premiacao.delete(id_prem)

                elif escolha == "3":
                    if(premiacao.get_all()):
                        print()
                        premiacao.print()
                        print()
                        id_premiacao = input("Digite o ID da premiação a ser atualizada: ")
                        nome_premiacao = input("Digite o novo nome da premiação: ")
                        ano_premiacao = input("Digite o novo ano da premiação: ")
                        premiacao.update(id_premiacao, nome_premiacao, ano_premiacao)

                elif escolha == "4":
                    id_prem = input("Digite o ID da premiação a ser buscada: ")
                    p = premiacao.get_by_id(id_prem)
                    if p:
                        print()
                        print(f"{p[0][0]} - {p[0][1]}, {p[0][2]}")
    
                elif escolha == "5":
                    if(premiacao.get_all()):
                        print()
                        premiacao.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "5":
             while True:
                print("\n-------- MENU INDICAÇÃO A PREMIAÇÃO --------")
                print("1 - Inserir Indicação")
                print("2 - Deletar Indicação")
                print("3 - Atualizar Indicação")
                print("4 - Buscar Indicação por ID")
                print("5 - Listar Todas as Indicações")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print()
                    filme.print(diretor, genero)
                    print()
                    id_filme = input("Digite o ID do filme: ")
                    print()
                    premiacao.print()
                    print()
                    id_premiacao= input("Digite o ID da premiação: ")
                    ganhou = input("O filme ganhou a premiação? (True ou False): ")
                    indicacao_premiacao.insert(int(id_filme), int(id_premiacao), bool(ganhou))

                elif escolha == "2":
                    if(indicacao_premiacao.get_all()):
                        print()
                        indicacao_premiacao.print(filme, sala)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser deletado: ")
                        print()
                        premiacao.print()
                        print()
                        id_premiacao = input("Digite o ID da premiação a ser deletada: ")
                        print()
                        indicacao_premiacao.delete((int(id_filme), int(id_premiacao)))

                elif escolha == "3":
                    if(indicacao_premiacao.get_all()):
                        print()
                        indicacao_premiacao.print(filme, sala)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser atualizado: ")
                        print()
                        premiacao.print()
                        print()
                        id_premiacao = input("Digite o ID da premiação a ser atualizada: ")
                        print()
                        ganhou = input("O filme ganhou a premiação? (True ou False): ")
                        indicacao_premiacao.update((int(id_filme), int(id_premiacao)), ganhou)

                elif escolha == "4":
                    id_premi = input("Digite o ID da premiação a ser buscada (id_filme,id_premiacao): ")
                    id_premi = tuple(map(int, id_premi.split(',')))
                    i = indicacao_premiacao.get_by_id(id_premi)
                    if i:
                        print()
                        sql = f"""SELECT nome FROM cinema.filme WHERE id = {i[0][0]}"""
                        sql_filme = filme.query(sql)
                        sql = f"""SELECT nome FROM cinema.premiacao WHERE id = {i[0][1]}"""
                        sql_premiacao = sala.query(sql)
                        if i[0][2] == True:
                            print(f"{sql_filme[0][0]}, {sql_premiacao[0][0]}, Ganhou")
                        else:
                            print(f"{sql_filme[0][0]}, {sql_premiacao[0][0]}, Perdeu")
    
                elif escolha == "5":
                    if(indicacao_premiacao.get_all()):
                        print()
                        indicacao_premiacao.print(filme, sala)
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "6":
            while True:
                print("\n-------- MENU SALA --------")
                print("1 - Inserir Sala")
                print("2 - Deletar Sala")
                print("3 - Atualizar Sala")
                print("4 - Buscar Sala por ID")
                print("5 - Listar Todos as Salas")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    nome_sala = input("Digite o nome da sala: ")
                    capacidade_sala = input("Digite a capacidade da sala: ")
                    sala.insert(nome_sala, capacidade_sala)

                elif escolha == "2":
                    if(sala.get_all()):
                        print()
                        sala.print()
                        print()     
                        id_sala = input("Digite o ID da sala a ser deletado: ")
                        sala.delete(id_sala)

                elif escolha == "3":
                    if(sala.get_all()):
                        print()
                        sala.print()
                        print()
                        id_sala = input("Digite o ID da sala a ser atualizada: ")
                        nome_sala = input("Digite o novo nome da sala: ")
                        capacidade_sala = input("Digite a nova capacidade da sala: ")
                        sala.update(id_sala, nome_sala, capacidade_sala)

                elif escolha == "4":
                    id_sala = input("Digite o ID da sala a ser buscada: ")
                    s = sala.get_by_id(id_sala)
                    if s:
                        print()
                        print(f"{s[0][0]} - {s[0][1]}, {s[0][2]}")
    
                elif escolha == "5":
                    if(sala.get_all()):
                        print()
                        sala.print()
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "7":
             while True:
                print("\n-------- MENU HORAŔIO --------")
                print("1 - Inserir Horário")
                print("2 - Deletar Horário")
                print("3 - Atualizar Horário")
                print("4 - Buscar Horário por ID")
                print("5 - Listar Todos as Horários")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    hora = input("Digite o horário: ")
                    horario.insert(hora)

                elif escolha == "2":
                    if(horario.get_all()):
                        print()
                        horario.print()
                        print()     
                        id_horario = input("Digite o ID do horário a ser deletado: ")
                        horario.delete(id_horario)

                elif escolha == "3":
                    if(horario.get_all()):
                        print()
                        horario.print()
                        print()
                        id_horario = input("Digite o ID do horário a ser atualizado: ")
                        hora = input("Digite o novo horário: ")
                        horario.update(id_horario, hora)

                elif escolha == "4":
                    id_horario = input("Digite o ID do horário a ser buscado: ")
                    h = horario.get_by_id(id_horario)
                    if h:
                        print(f"{h[0][0]} - {h[0][1]}")
    
                elif escolha == "5":
                    if(horario.get_all()):
                        print()
                        horario.print()
    
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "8": # Exibição
            while True:
                print("\n-------- MENU EXIBIÇÃO --------")
                print("1 - Inserir Exibição")
                print("2 - Deletar Exibição")
                print("3 - Atualizar Exibição")
                print("4 - Buscar Exibição por ID")
                print("5 - Listar Todas as Exibições")
                print("6 - Voltar")

                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    print()
                    filme.print(diretor, genero)
                    print()
                    id_filme = input("Digite o ID do filme: ")
                    print()
                    sala.print()
                    print()
                    id_sala= input("Digite o ID da sala: ")
                    print()
                    horario.print()
                    print()
                    id_horario = input("Digite o ID do horário: ")
                    data = input("Digite a data da exibição(ano-mês-dia): ")
                    exibicao.insert(id_filme, id_sala, id_horario, data)

                elif escolha == "2":
                    if(exibicao.get_all()):
                        print()
                        exibicao.print(filme, sala, horario)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser deletado: ")
                        print()
                        sala.print()
                        print()
                        id_sala = input("Digite o ID da sala a ser deletada: ")
                        print()
                        horario.print()
                        print()
                        id_horario = input("Digite o ID do horário a ser deletado: ")
                        exibicao.delete((int(id_filme), int(id_sala), int(id_horario)))

                elif escolha == "3":
                    if(exibicao.get_all()):
                        print()
                        exibicao.print(filme, sala, horario)
                        print()
                        filme.print(diretor, genero)
                        print()  
                        id_filme = input("Digite o ID do filme a ser atualizado: ")
                        print()
                        sala.print()
                        print()
                        id_sala = input("Digite o ID da sala a ser atualizada: ")
                        print()
                        horario.print()
                        print()
                        id_horario = input("Digite o ID do horário a ser atualizado: ")
                        data = input("Digite a nova data: ")
                        exibicao.update((int(id_filme), int(id_sala), int(id_horario)), data)

                elif escolha == "4":
                    id_exib = input("Digite o ID da exibição a ser buscada (id_filme,id_sala,id_horario): ")
                    id_exib = tuple(map(int, id_exib.split(',')))
                    e = exibicao.get_by_id(id_exib)
                    if e:
                        sql = f"""SELECT nome FROM cinema.filme WHERE id = {e[0][0]}"""
                        sql_filme = filme.query(sql)
                        sql = f"""SELECT nome FROM cinema.sala WHERE id = {e[0][1]}"""
                        sql_sala = sala.query(sql)
                        sql = f"""SELECT horario FROM cinema.horario WHERE id = {e[0][2]}"""
                        sql_horario = horario.query(sql)
                        print(f"{sql_filme[0][0]}, {sql_sala[0][0]}, {sql_horario[0][0]}")
    
                elif escolha == "5":
                    if(exibicao.get_all()):
                        print()
                        exibicao.print(filme, sala, horario)
                elif escolha == "6":
                    break
                else:
                    print("Opção inválida. Tente novamente.")

        elif opcao == "9":
            while True:
                print("\n-------- MENU SQL --------")
                print("1 - Número de filmes dirigidos por cada diretor")
                print("2 - ")
                print("3 - ")
                print("4 - Voltar")
        
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    # Consulta para contar o número de filmes dirigidos por cada diretor:
                    sql = """SELECT cinema.diretor.nome, COUNT(cinema.filme.id) AS total_filmes
                            FROM cinema.diretor
                            LEFT JOIN cinema.filme ON cinema.diretor.id = cinema.filme.id_diretor
                            GROUP BY cinema.diretor.nome;"""
            
                    data = connection.query(sql)
                    print(data)

                elif escolha == "2":
                    # Consulta para calcular o número total de exibições por sala e horário:
                    sql = """SELECT cinema.sala.nome, cinema.horario.hora, COUNT(cinema.exibicao.id) AS total_exibicoes
                            FROM cinema.exibicao
                            JOIN cinema.sala ON cinema.exibicao.id_sala = cinema.sala.id
                            JOIN cinema.horario ON cinema.exibicao.id_horario = cinema.horario.id
                            GROUP BY cinema.sala.nome, cinema.horario.hora;"""

                    data = connection.query(sql)
                    print(data)

                elif escolha == "3":
                    # Consulta para listar todos os filmes, incluindo aqueles que não foram indicados a nenhuma premiação, e as premiações associadas a cada filme
                    sql = """SELECT cinema.filme.nome, cinema.premiacao.nome AS premiacao
                            FROM cinema.filme
                            LEFT JOIN cinema.indicacao_premiacao ON cinema.filme.id = cinema.indicacao_premiacao.id_filme
                            LEFT JOIN cinema.premiacao ON cinema.indicacao_premiacao.id_premiacao = cinema.premiacao.id;"""
                    
                    data = connection.query(sql)
                    print(data)

                elif escolha == "4":
                    break

                else:
                    print("Opção inválida. Tente novamente.")


        elif opcao == "10":
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


