from model import disciplina
import streamlit as st

# Classe responsável por gerenciar as telas do sistema
class Tela_disciplina():

    def __init__(self):
        # Instanciando nome da disciplina, professor da disciplina e carga horária da disciplina
        self.nome_disciplina = None
        self.professor_disciplina = None
        self.carga_horaria = None
        self.disciplina = disciplina.Disciplina(self.nome_disciplina, self.professor_disciplina, self.carga_horaria)

    # Método responsável por gerenciar a tela de disciplina
    def tela_disciplina(self):

        st.title("Área da Disciplina")
        box_disciplina = st.selectbox("Selecione uma opção:", ("Cadastrar", "Editar", "Excluir", "Listar"))

        match box_disciplina:
            
            case "Cadastrar":

                st.title("Cadastrar Disciplina")
                st.markdown("Preencha os campos abaixo:")
                self.nome_disciplina = st.text_input("Nome")
                self.professor_disciplina = st.text_input("Professor")
                self.carga_horaria = st.number_input("Carga Horária")
                bt_cadastrar = st.button("Cadastrar")

                if bt_cadastrar:
                    if self.disciplina.cadastro_disciplina(self.nome_disciplina, self.professor_disciplina, self.carga_horaria):
                        st.success("Disciplina cadastrada com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao cadastrar disciplina!")
                        st.stop()


            case "Editar":

                st.title("Editar Disciplina")
                bt_mostrar = st.button("Mostrar Lista de Disciplinas")

                if bt_mostrar:
                    st.table(self.disciplina.listar_disciplina())
                

                st.markdown("Preencha os campos abaixo:")
                self.nome_disciplina = st.text_input("Nome da Disciplina a ser editada")
                
                novo_nome_disciplina = st.text_input("Novo Nome da Disciplina")
                self.professor_disciplina = st.text_input("Novo Professor")
                self.carga_horaria = st.number_input("Nova Carga Horária")
                bt_editar = st.button("Editar")

                if bt_editar:
                    if self.disciplina.editar_disciplina(self.nome_disciplina, novo_nome_disciplina, self.professor_disciplina, self.carga_horaria):
                        st.success("Disciplina editada com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao editar disciplina!")
                        st.stop()


            case "Excluir":

                st.title("Excluir Disciplina")
                bt_mostrar = st.button("Mostrar Lista de Disciplinas")

                if bt_mostrar:
                    st.table(self.disciplina.listar_disciplina())
                
                self.nome_disciplina = st.text_input("Nome da Disciplina a ser excluída")
                bt_excluir = st.button("Excluir")

                if bt_excluir:
                    if self.disciplina.excluir_disciplina(self.nome_disciplina):
                        st.success("Disciplina excluída com sucesso!")
                        st.stop()
                    else:
                        st.error("Erro ao excluir disciplina!")
                        st.stop()
            

            case "Listar":

                st.title("Listar Disciplinas")
                bt_mostrar = st.button("Mostrar Lista de Disciplinas")

                if bt_mostrar:
                    st.table(self.disciplina.listar_disciplina())