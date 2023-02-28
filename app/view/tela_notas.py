import streamlit as st
from model import notas

# Classe responsável por gerenciar as telas do sistema
class Tela_notas():

    def __init__(self):
        # Instanciando nome do aluno, nome da disciplina e nota do aluno
        self.nome_aluno = None
        self.nome_disciplina = None
        self.nota_aluno = None
        self.nota = notas.Notas()
    
    # Método responsável por gerenciar a tela de notas
    def tela_notas(self):

        st.title("Sessão de Notas")
        st.markdown("Selecione uma opção")
        box_notas = st.selectbox("Selecione uma opção", ("Cadastrar", "Editar", "Excluir", "Listar"))
        
        match box_notas:

            case "Cadastrar":
                st.title("Cadastrar Notas")
                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome do Aluno")
                self.nome_disciplina = st.text_input("Nome da Disciplina")
                self.nota_aluno = st.number_input("Nota")
                bt_cadastrar = st.button("Cadastrar")

                if bt_cadastrar:
                    if self.nota.cadastro_notas(self.nome_aluno, self.nome_disciplina, self.nota_aluno):
                        st.success("Nota cadastrada com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao cadastrar nota!")
                        st.stop()

            
            case "Editar":
                st.title("Editar Notas")
                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome do Aluno a ser editado")
                self.nome_disciplina = st.text_input("Nome da Disciplina a ser editada")
                st.markdown("Informações a serem editadas:")
                nova_nota_aluno = st.number_input("Nova Nota")
                bt_editar = st.button("Editar")

                if bt_editar:
                    if self.nota.editar_notas(self.nome_aluno, self.nome_disciplina, nova_nota_aluno):
                        st.success("Nota editada com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao editar nota!")
                        st.stop()
                        
            
            case "Excluir":
                st.title("Excluir Notas")
                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome do Aluno")
                self.nome_disciplina = st.text_input("Nome da Disciplina")
                bt_excluir = st.button("Excluir")

                if bt_excluir:
                    if self.nota.excluir_notas(self.nome_aluno, self.nome_disciplina):
                        st.success("Nota excluída com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao excluir nota!")
                        st.stop()

        
            case "Listar":
                st.title("Listar Notas por Matéria")
                st.markdown("Preencha os campos abaixo:")
                self.nome_disciplina = st.text_input("Nome da Disciplina")
                bt_mostrar = st.button("Mostrar Lista de Notas")


                if bt_mostrar:
                    st.table(self.nota.listar_notas_por_disciplina(self.nome_disciplina))