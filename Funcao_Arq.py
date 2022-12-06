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