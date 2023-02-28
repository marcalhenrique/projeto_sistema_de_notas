import streamlit as st
from model import professor


# Classe responsável por gerenciar as telas do sistema
class Tela_professor():
    def __init__(self):
        # Instanciando nome e area do professor
        self.nome_professor = None
        self.area_professor = None
        self.professor = professor.Professor(self.nome_professor, self.area_professor) # Instanciando a classe Professor
        

    # Método responsável por gerenciar a tela de professor
    def tela_professor(self):
            
            st.title("Área do Professor")
            st.markdown("Selecione uma opção:")
            box_professor = st.selectbox("Selecione uma opção", ("Cadastrar", "Editar", "Excluir", "Listar"))

            # Switch case para selecionar a tela de acordo com a opção selecionada no menu do professor
            match box_professor:

                case "Cadastrar":
                    st.title("Cadastrar Professor")
                    st.markdown("Preencha os campos abaixo:")
                    self.nome_professor = st.text_input("Nome")
                    self.area_professor = st.text_input("Área de Atuação")
                    bt_cadastrar = st.button("Cadastrar")
                    
                    if bt_cadastrar:
                        if self.professor.cadastro_professor(self.nome_professor, self.area_professor):
                            st.success("Professor cadastrado com sucesso!")
                            st.stop()
                        else:
                            st.error("Erro ao cadastrar professor!")
                            st.stop()

                    
                case "Editar":
                    st.title("Editar Professor")
                    bt_mostrar = st.button("Mostrar Lista de Professores")
                    
                    if bt_mostrar:
                        st.table(self.professor.listar_professor())

                    st.markdown("Preencha os campos abaixo:")
                    self.nome_professor = st.text_input("Nome do Professor a ser editado")
                    st.markdown("Informações a serem editadas:")
                    novo_nome_professor = st.text_input("Novo Nome")
                    self.area_professor = st.text_input("Nova Área de Atuação")
                    bt_editar = st.button("Editar")

                    if bt_editar:
                        if self.professor.editar_professor(self.nome_professor, novo_nome_professor, self.area_professor):
                            st.success("Professor editado com sucesso!")
                            st.stop()
                        else:
                            st.error("Erro ao editar professor!")
                            st.stop()

                      
                case "Excluir":
                    st.title("Excluir Professor")
                    bt_mostrar = st.button("Mostrar Lista de Professores")

                    if bt_mostrar:
                        st.table(self.professor.listar_professor())

                    st.markdown("Preencha os campos abaixo:")
                    self.nome_professor = st.text_input("Nome do Professor a ser excluído")
                    bt_excluir = st.button("Excluir")

                    if bt_excluir:
                        if self.professor.excluir_professor(self.nome_professor):
                            st.success("Professor excluído com sucesso!")
                            st.stop()
                        else:
                            st.error("Erro ao excluir professor!")
                            st.stop()
                            
            
                case "Listar":
                    st.title("Listar Professor")
                    st.markdown("Preencha os campos abaixo:")
                    bt_listar = st.button("Listar Professor")
                    if bt_listar:
                        st.table(self.professor.listar_professor())
                        st.stop()