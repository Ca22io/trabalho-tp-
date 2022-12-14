import json
import os.path

nome_arquivo = 'livros.json'


def ler_arquivo():
    if not os.path.isfile(nome_arquivo):
        criarArquivo()

    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()

    if len(data) == 0:
        return []

    data = json.loads(data)
    arq.close()

    return data


def salvarArquivo(livros: list):
    arq = open('livros.json', 'w+', encoding='utf-8')
    data = json.dumps(livros, indent=5)
    arq.write(data)
    arq.close()


def criarArquivo():
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    arq.close()
