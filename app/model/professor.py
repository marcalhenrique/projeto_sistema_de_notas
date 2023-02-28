import pandas as pd
from controller import connect_postgresql as connection


# Classe responsável por manipular os dados da tabela professor
class Professor():

    def __init__(self, nome_professor, area_professor):
        # conexao criada dentro do construtor para que a conexão seja criada toda vez que um objeto for instanciado
        self.conexao = connection.ConnectPostgresql()
        self.conexao.connect()
        self.nome_professor = nome_professor 
        self.area_professor = area_professor


    def cadastro_professor(self, nome_professor, area_professor): 

        self.conexao.curs.execute(f"INSERT INTO professor (nome_professor, area) VALUES (%s, %s)", (nome_professor, area_professor))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
    

    def editar_professor(self, novo_nome_professor, nome_professor, area_professor):
        
        self.conexao.curs.execute(f"UPDATE professor SET nome_professor = %s, area = %s WHERE nome_professor = %s", (nome_professor, area_professor, novo_nome_professor))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True

 
    def excluir_professor(self, nome_professor):

        self.conexao.curs.execute(f"DELETE FROM professor WHERE nome_professor = %s;", (nome_professor,))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
        

    def listar_professor(self):
     
        df_professores = pd.read_sql_query("SELECT nome_professor, area FROM professor", self.conexao.conn)
        df_professores = df_professores.rename(columns={"nome_professor": "Nome do Professor", "area": "Área de Atuação"})
        self.conexao.conn.close()
        return df_professores
                