from controller import connect_postgresql as connection
import pandas as pd

# Classe responsável por manipular os dados da tabela aluno
class Disciplina():
    
    def __init__(self, nome_disciplina, professor_disciplina, carga_horaria):
        # Instanciando a classe de conexão, nome do aluno, data de nascimento e média
        self.conexao = connection.ConnectPostgresql()
        self.conexao.connect()
        self.nome_disciplina = nome_disciplina
        self.carga_horaria = carga_horaria
        self.professor_disciplina  = professor_disciplina


    def cadastro_disciplina(self, nome_disciplina, professor_disciplina, carga_horaria):

        self.conexao.curs.execute(f"SELECT id_professor FROM professor WHERE nome_professor = '{professor_disciplina}'")
        id_professor = self.conexao.curs.fetchone()

        if id_professor is None:
            return False
        else:
            self.conexao.curs.execute(f"INSERT INTO disciplina (nome_disciplina, id_professor, carga_horaria) VALUES ('{nome_disciplina}', {id_professor[0]}, {carga_horaria})")
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
    
    def editar_disciplina(self, nome_disciplina, novo_nome_disciplina, professor_disciplina, carga_horaria):

        self.conexao.curs.execute(f"SELECT id_professor FROM professor WHERE nome_professor = '{professor_disciplina}'")
        id_professor = self.conexao.curs.fetchone()

        if id_professor is None:
            return False
        else:
            self.conexao.curs.execute(f"UPDATE disciplina SET nome_disciplina = %s, id_professor = %s, carga_horaria = %s WHERE nome_disciplina = %s", (novo_nome_disciplina, id_professor[0], carga_horaria, nome_disciplina))
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
    
    def excluir_disciplina(self, nome_disciplina):

        self.conexao.curs.execute(f"DELETE FROM disciplina WHERE nome_disciplina = %s", (nome_disciplina,))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
    

    def listar_disciplina(self):
        
        df_disciplina = pd.read_sql_query("SELECT nome_disciplina, nome_professor, carga_horaria FROM disciplina INNER JOIN professor ON disciplina.id_professor = professor.id_professor", self.conexao.conn)
        df_disciplina = df_disciplina.rename(columns={"nome_disciplina": "Nome da Disciplina", "nome_professor": "Professor", "carga_horaria": "Carga Horária"})
        self.conexao.conn.close()
        return df_disciplina
    
    
        
   