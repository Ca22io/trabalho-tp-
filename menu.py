from funcao_livro import *


while True:
    escolha = menu()

    if escolha == 1:
         cadastrar_livr()

    elif escolha == 2:
        alterar_livr()

    elif escolha == 3:
         deletar_livr()

    elif escolha == 4:
         pesquisar_livr()

    elif escolha == 5:
         lista_livr()
    
    elif escolha == 6:
        break