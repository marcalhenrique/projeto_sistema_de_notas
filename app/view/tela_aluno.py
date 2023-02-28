import streamlit as st
from model import aluno

# Classe responsável por gerenciar as telas do sistema
class Tela_aluno():

    def __init__(self):
        # Instanciando nome do aluno, data de nascimento e média do aluno
        self.nome_aluno = None
        self.data_nascimento = None
        self.media = None
        self.aluno = aluno.Aluno(self.nome_aluno, self.data_nascimento, self.media)

    # Método responsável por gerenciar a tela de aluno
    def tela_aluno(self):

        st.title("Área do Aluno")
        box_aluno = st.selectbox("Selecione uma opção:", ("Cadastrar", "Editar", "Excluir", "Calcular Média", "Listar"))

        match box_aluno:

            case "Cadastrar":

                st.title("Cadastrar Aluno")
                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome")
                self.data_nascimento = st.date_input("Data de Nascimento")
                bt_cadastrar = st.button("Cadastrar")

                if bt_cadastrar:
                    if self.aluno.cadastro_aluno(self.nome_aluno, self.data_nascimento):
                        st.success("Aluno cadastrado com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao cadastrar aluno!")
                        st.stop()

            
            case "Editar":

                st.title("Editar Aluno")
                bt_mostrar = st.button("Mostrar Lista de Alunos")

                if bt_mostrar:
                    st.table(self.aluno.listar_aluno())
                
                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome do Aluno a ser editado")
                st.markdown("Informações a serem editadas:")
                novo_nome_aluno = st.text_input("Novo Nome")
                self.data_nascimento = st.date_input("Nova Data de Nascimento")
                bt_editar = st.button("Editar")

                if bt_editar:
                    if self.aluno.editar_aluno(self.nome_aluno, novo_nome_aluno, self.data_nascimento):
                        st.success("Aluno editado com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao editar aluno!")
                        st.stop()

            
            case "Excluir":

                st.title("Excluir Aluno")
                bt_mostrar = st.button("Mostrar Lista de Alunos")

                if bt_mostrar:
                    st.table(self.aluno.listar_aluno())

                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome do Aluno a ser excluído")
                bt_excluir = st.button("Excluir")

                if bt_excluir:
                    if self.aluno.excluir_aluno(self.nome_aluno):
                        st.success("Aluno excluído com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao excluir aluno!")
                        st.stop()

            
            case "Calcular Média":

                st.title("Calcular Média")
                bt_mostrar = st.button("Mostrar Lista de Alunos")

                if bt_mostrar:
                    st.table(self.aluno.listar_aluno())
                
                st.markdown("Preencha os campos abaixo:")
                self.nome_aluno = st.text_input("Nome do Aluno")
                bt_calcular = st.button("Calcular Média")

                if bt_calcular:
                    if self.aluno.calcular_media(self.nome_aluno):
                        st.success("Média calculada com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao calcular média!")
                        st.stop()


            case "Listar":

                st.title("Lista de Alunos")
                bt_mostrar = st.button("Mostrar Lista de Alunos")

                if bt_mostrar:
                    st.table(self.aluno.listar_aluno())