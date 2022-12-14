import os
from Funcao_Arq import *

class Livro:
    nome:str
    
    genero:str

    autor:str

    paginas:int

    ano:int

    def cadastro_livro(self) -> dict:
        livro = {}
        
        livro["nome"] = self.nome
        livro["genero"] = self.genero
        livro["autor"] = self.autor
        livro["paginas"] = self.paginas
        livro["ano"] = self.ano

        return livro

class Alterar:
    def  mudar():
        lista = ler_arquivo()
        nome = input('Qual livro deseja alterar?')
        for p in lista: 
            if p['nome'] == nome :
                p["nome"]=input("Qual o nome: ")
                
                p["genero"]=input("Qual o gênero: ")

                p["autor"]=input("Qual o autor: ")

                p["paginas"]=int(input("Quantidade páginas: "))

                p["ano"]=int(input("Qual o ano de lançamento: "))
        
        print("\033[1;32mAlterado com sucesso!\033[m")

        salvarArquivo(lista)      



class Deletar:
    def  remover():
        os.system('clear' if os.name == 'posix' else 'cls')
        lista = ler_arquivo()
        nome = input('Qual livro deseja alterar?')
        for p in lista: 
            if p['nome'] == nome :
                lista.remove(p)
        
        print('Livro removido!')

        input("Presione ENTER para continuar!")
        
        salvarArquivo(lista)        


class Pesquisar:
    def print_livro():
        os.system('clear' if os.name == 'posix' else 'cls')
        lista = ler_arquivo()
        nome = input('Qual nome deseja pesquisar?')
        for p in lista: 
            if p['nome'] == nome :
                print("\033[1;32m=-=\033[m"*10)

                print(f'\033[1;33mNome: \033[m{p["nome"]}')
                
                print(f'\033[1;33mGênero: \033[m{p["genero"]}')
                
                print(f'\033[1;33mAutor: \033[m{p["autor"]}')
                
                print(f'\033[1;33mPagínas: \033[m{p["paginas"]}')
                
                print(f'\033[1;33mAno de lançamento: \033[m{p["ano"]}')
                
                print("\033[1;32m=-=\033[m"*10)
            
        input("Presione ENTER para continuar!")


class Listar:
   def todos():
        os.system('clear' if os.name == 'posix' else 'cls') 
        lista = ler_arquivo() 

        if len(lista) == 0 :
            print('Não há livros cadastrados!!')
            
        else:
            for i in range(len(lista)):
                print(f"\033[1;32m-=--=-\033[m \033[1;31m  {lista [i]['nome']}  \033[m \033[1;32m-=--=-\033[m")
                
                print(f"\033[1;33mGênero: \033[m{lista [i]['genero']}")
                
                print(f"\033[1;33mAutor: \033[m{lista [i]['autor']}")
                
                print(f"\033[1;33mPagínas: \033[m{lista [i]['paginas']}")
                
                print(f"\033[1;33mAno de lançamento: \033[m{lista [i]['ano']}")

        input("Presione ENTER para continuar!")
