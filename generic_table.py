from connection import Connection

class GenericTable(Connection):
    def __init__(self):
        Connection.__init__(self)
    
    def create_table(self, sql):
        try:
            self.execute(sql)
            self.commit()
            print("Tabela criada")
        except Exception as e:
            print("Erro ao criar a tabela ", e)

    def drop_table(self, table_name):
        try:
            sql = f"""drop table {table_name} CASCADE;"""
            self.execute(sql)
            self.commit()
            print("Tabela deletada")
        except Exception as e:
            print("Erro ao deletar a tabela ", e)

    def insert(self, sql, *args):
        try:
            self.execute(sql, args)
            self.commit()
            print("Registro inserido")
        except Exception as e:
            print("Erro ao inserir ", e)

    def delete(self, sql):
        try:
            self.execute(sql)
            self.commit()
            print("Registro deletado")
        except Exception as e:
            print("Erro ao deletar ", e)
    
    def update(self, sql, *args):
        try:
            self.execute(sql, args)
            self.commit()
            print("Registro atualizado")
        except Exception as e:
            print("Erro ao atualizar ", e)

    def get_by_id(self, sql):
        data = self.query(sql)
        if data:
            return data
        else:
            print("Registro não encontrado")
            return 

    def get_all(self, table_name):
        sql = f"SELECT * FROM {table_name}"
        data = self.query(sql)
        if data:
            return data
        else:
            print("Registros não encontrados")
            return 
