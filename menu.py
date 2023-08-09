from funcoes import *
import os

class Menu():
    def grid_escolha():
        os.system('cls')
        print("\033[1;32m-=-\033[m"*10)
    
        print('         \033[4mMenu inicial\033[m')
        
        print("\033[1;32m-=-\033[m"*10)
        
        print('\033[1;32m-=-\033[m  \033[1m1 - Cadastrar livro\033[m   \033[1;32m-=-\033[m')
        
        print('\033[1;32m-=-\033[m  \033[1m2 - Alterar livro\033[m     \033[1;32m-=-\033[m')
        
        print('\033[1;32m-=-\033[m  \033[1m3 - Deletar livro\033[m     \033[1;32m-=-\033[m')
        
        print('\033[1;32m-=-\033[m  \033[1m4 - Pesquisar livro\033[m   \033[1;32m-=-\033[m')
        
        print('\033[1;32m-=-\033[m  \033[1m5 - Listar livros\033[m     \033[1;32m-=-\033[m')
        
        print('\033[1;32m-=-\033[m  \033[1m6 - Sair\033[m              \033[1;32m-=-\033[m')
        
        print("\033[1;32m-=-\033[m"*10)
        
        return int(input('Escolha uma opção: '))

menu = Menu()
while True:
    escolha = menu(grid_escolha)

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
