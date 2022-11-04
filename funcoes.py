import os
import json

def ler_arquivo() -> list:
    arq = open('livros.json', 'r', encoding='utf-8')
    data = arq.read()
    return json.loads(data)

def salvarArquivo(livros: list):
    arq = open('livros.json', 'w+', encoding='utf-8')
    data = json.dumps(livros, indent=5)
    arq.write(data)
    arq.close()

def cadastrar_livr()-> dict:
     livro = {}
    
     livro["nome"]=input("Qual o nome: ")
    
     livro["genero"]=input("Qual o gênero: ")

     livro["autor"]=input("Qual o autor: ")

     livro["paginas"]=int(input("Quantidade páginas: "))

     livro["ano"]=int(input("Qual o ano de lançamento: "))
    
     livros = ler_arquivo()
     livros.append(livro)
     salvarArquivo(livros)
 
def menu():
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
    

def  alterar_livr():
    os.system('cls')
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

def  deletar_livr():
    os.system('cls')
    lista = ler_arquivo()
    nome = input('Qual livro deseja alterar?')
    for p in lista: 
        if p['nome'] == nome :
            lista.remove(p)
    
    salvarArquivo(lista)        



def pesquisar_livr():
    os.system('cls')
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

def lista_livr():
    os.system('cls') 
    lista = ler_arquivo()
    for i in range(len(lista)):
        print(f"\033[1;32m-=--=-\033[m \033[1;31m  {lista [i]['nome']}  \033[m \033[1;32m-=--=-\033[m")
        
        print(f"\033[1;33mGênero: \033[m{lista [i]['genero']}")
        
        print(f"\033[1;33mAutor: \033[m{lista [i]['autor']}")
        
        print(f"\033[1;33mPagínas: \033[m{lista [i]['paginas']}")
        
        print(f"\033[1;33mAno de lançamento: \033[m{lista [i]['ano']}")

    input("Presione ENTER para continuar!")