#----------------------------------------------------------------------
# Marçal Henrique Moreira
# Discente em Engenharia de Computação pelo IFMG - Campus Bambuí
# 2022
# Abaeté - MG
# github.com/marcalhenrique
#----------------------------------------------------------------------
'''
--- Projeto de Estudo: Sistema de Gerenciamento de Notas ---

Sistema de gerenciamento de notas de alunos de uma escola utilizando a biblioteca Streamlit para a interface gráfica
e o PostgreSQL para armazenamento dos dados, rodando em container Docker.
Projeto desenvolvido para o aprendizado de Docker, utilizando o docker-compose para a criação dos containers. Mais detalhes no 
arquivo README.md do repositório.
'''

from view import tela_menu

def main():
    menu = tela_menu.TelaMenu()
    menu.menu()



if __name__ == '__main__':
    main()