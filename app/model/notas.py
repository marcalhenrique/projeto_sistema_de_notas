from controller import connect_postgresql as conn
import pandas as pd

# Classe responsável por manipular os dados da tabela notas
class Notas():

    def __init__(self):
        # Instanciando a classe de conexão, nome do aluno, nome da disciplina e nota
        self.conexao = conn.ConnectPostgresql()
        self.conexao.connect()
        self.nome_aluno = None
        self.nome_disciplina = None
        self.nota = None
    

    def cadastro_notas(self, nome_aluno, nome_disciplina, nota):
        
        id_disciplina = self.conexao.curs.execute(f"SELECT id_disciplina FROM disciplina WHERE nome_disciplina = %s", (nome_disciplina,))
        id_disciplina = self.conexao.curs.fetchone()
        id_aluno = self.conexao.curs.execute(f"SELECT id_aluno FROM aluno WHERE nome_aluno = %s", (nome_aluno,))
        id_aluno = self.conexao.curs.fetchone()

        self.conexao.curs.execute(f"INSERT INTO matriculado (id_aluno, id_disciplina, nota) VALUES (%s, %s, %s)", (id_aluno, id_disciplina, nota))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
        
    
    def editar_notas(self, nome_aluno, nome_disciplina, nova_nota_aluno):

        id_disciplina = self.conexao.curs.execute(f"SELECT id_disciplina FROM disciplina WHERE nome_disciplina = %s", (nome_disciplina,))
        id_disciplina = self.conexao.curs.fetchone()
        id_aluno = self.conexao.curs.execute(f"SELECT id_aluno FROM aluno WHERE nome_aluno = %s", (nome_aluno,))
        id_aluno = self.conexao.curs.fetchone()

        self.conexao.curs.execute(f"UPDATE matriculado SET nota = %s WHERE id_aluno = %s AND id_disciplina = %s", (nova_nota_aluno, id_aluno, id_disciplina))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True
        

    def excluir_notas(self, nome_aluno, nome_disciplina):

        id_disciplina = self.conexao.curs.execute(f"SELECT id_disciplina FROM disciplina WHERE nome_disciplina = %s", (nome_disciplina,))
        id_disciplina = self.conexao.curs.fetchone()
        id_aluno = self.conexao.curs.execute(f"SELECT id_aluno FROM aluno WHERE nome_aluno = %s", (nome_aluno,))
        id_aluno = self.conexao.curs.fetchone()

        self.conexao.curs.execute(f"UPDATE matriculado SET nota = 0 WHERE id_aluno = %s AND id_disciplina = %s", (id_aluno, id_disciplina))
        if self.conexao.curs.rowcount == 0:
            return False
        else:
            self.conexao.conn.commit()
            self.conexao.conn.close()
            return True


    def listar_notas_por_disciplina(self, nome_disciplina):
        id_disciplina = self.conexao.curs.execute(f"SELECT id_disciplina FROM disciplina WHERE nome_disciplina = %s", (nome_disciplina,))
        id_disciplina = self.conexao.curs.fetchone()
        df_notas = pd.read_sql_query("SELECT nome_aluno, nota FROM aluno a, matriculado m WHERE a.id_aluno = m.id_aluno AND m.id_disciplina = %s;", self.conexao.conn, params=(id_disciplina))
        df_notas = df_notas.rename(columns={"nome_aluno": "Nome do Aluno", "nota": "Nota"})
        return df_notas

