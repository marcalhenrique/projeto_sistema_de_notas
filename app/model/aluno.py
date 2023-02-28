from controller import connect_postgresql as connection
import pandas as pd

# Classe responsável por manipular os dados da tabela aluno
class Aluno():

    def __init__(self, nome_aluno, data_nascimento, media):
        # Instanciando a classe de conexão, nome do aluno, data de nascimento e média
        self.conexao = connection.ConnectPostgresql()
        self.conexao.connect()
        self.nome_aluno = nome_aluno
        self.data_nascimento = data_nascimento
        self.media = media

    
    def cadastro_aluno(self, nome_aluno, data_nascimento):

        self.conexao.curs.execute(f"INSERT INTO aluno (nome_aluno, data_nascimento) VALUES (%s, %s)", (nome_aluno, data_nascimento))
        if self.conexao.curs.rowcount == 0: # Se não houver linhas afetadas, retorna falso
            return False
        else:
            self.conexao.conn.commit() # Se houver linhas afetadas, faz o commit e retorna verdadeiro
            self.conexao.conn.close() # Fecha a conexão
            return True
        
    
    def editar_aluno(self, novo_nome_aluno, nome_aluno, data_nascimento):

        self.conexao.curs.execute(f"UPDATE aluno SET nome_aluno = %s, data_nascimento = %s WHERE nome_aluno = %s", (nome_aluno, data_nascimento, novo_nome_aluno))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
        
            
    def excluir_aluno(self, nome_aluno):

        self.conexao.curs.execute(f"DELETE FROM aluno WHERE nome_aluno = %s;", (nome_aluno,))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True


    def calcular_media(self, nome_aluno):

        id_aluno = self.conexao.curs.execute(f"SELECT id_aluno FROM aluno WHERE nome_aluno = %s", (nome_aluno,))
        id_aluno = self.conexao.curs.fetchone()
        media = self.conexao.curs.execute(f"UPDATE aluno SET media = (SELECT AVG(nota) FROM matriculado WHERE id_aluno = %s) WHERE id_aluno = %s", (id_aluno, id_aluno))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True


    def listar_aluno(self):
        
        df_alunos = pd.read_sql_query("SELECT nome_aluno, data_nascimento, media FROM aluno", self.conexao.conn)
        df_alunos = df_alunos.rename(columns={"nome_aluno": "Nome do Aluno", "data_nascimento": "Data de Nascimento", "media": "Média"})
        self.conexao.conn.close()
        return df_alunos
    

