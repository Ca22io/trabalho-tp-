from Class import *
import os

class modulos():
    
    def cadastrar_livr()-> dict:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\033[1;32m--------\033[m \033[1mCadastro de Livro\033[m \033[1;32m--------\033[m")
        livro = Livro()
        
        livro.nome = input("Qual o nome: ")
        
        livro.genero = input("Qual o gênero: ")
    
        livro.autor = input("Qual o autor: ")
    
        livro.paginas = int(input("Quantidade páginas: "))
    
        livro.ano = int(input("Qual o ano de lançamento: "))
        
        livros = ler_arquivo()
        livros.append(livro.cadastro_livro())
    
        salvarArquivo(livros)
        
    def  alterar_livr():
        os.system('clear' if os.name == 'posix' else 'cls')
        print("\033[1;32m--------\033[m \033[1mEdição de Livro\033[m \033[1;32m--------\033[m")
        alterar = Alterar
        alterar.mudar()
    
    def  deletar_livr():
          deletar = Deletar
          deletar.remover()
    
    def pesquisar_livr():
        pesquisar = Pesquisar
        pesquisar.print_livro()
    
    def lista_livr():
        listar = Listar
        listar.todos()

