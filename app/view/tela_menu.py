import streamlit as st
from view import tela_professor, tela_aluno, tela_disciplina, tela_notas


# Classe responsável por gerenciar as telas do sistema
class TelaMenu():

    def __init__(self):
        # Instanciando as telas
        self.tela_professor = tela_professor.Tela_professor()
        self.tela_aluno = tela_aluno.Tela_aluno()
        self.tela_disciplina = tela_disciplina.Tela_disciplina()
        self.tela_notas = tela_notas.Tela_notas()

    def menu(self):

        # Tela de menu
        st.title("Sistemas de Notas")
        st.sidebar.title("Menu de Opções")
        menu = st.sidebar.selectbox("Selecione uma opção", ("Professor", "Aluno", "Disciplina", "Notas"))

        # Switch case para selecionar a tela de acordo com a opção selecionada no menu
        match menu:

            case "Professor":
                self.tela_professor.tela_professor()


            case "Aluno":
                self.tela_aluno.tela_aluno()

            
            case "Disciplina":
                self.tela_disciplina.tela_disciplina()

            
            case "Notas":
                self.tela_notas.tela_notas()