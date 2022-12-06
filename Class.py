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

# livro = Livro()

# livro.nome = 'cassio'

# livro.genero = 'Ação'

# livro.autor = 'cassio'

# livro.paginas = 123

# livro.ano = 2022

# print(livro.Tudo())