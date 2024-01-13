import os

from lib.interface import *


def arquivo_existente(nome):
    try:
        with open(nome, 'rt'):
            pass  # Não e preciso fazer nada, so estamos verificando se o arquivo existe
    except FileNotFoundError:
        print('O arquivo não foi Localizado! :(')
    else:
        print('O arquivo foi localizado com sucesso!')


def criar_arquivo(nome):
    if not os.path.exists(nome):
        try:
            with open(nome, 'wt+'):
                pass  # Não e preciso fazer nada pois aqui criamos o arquivo caso o mesmo não exista.
        except:
            print('Houve um ERRO: Ao criar o arquivo.')
        else:
            print(f'Arquivo {nome} criado com sucesso!')


def lerarquivo(nome):
    anotacoes = {}

    try:
        with open(nome, 'rt') as arquivo:
            cabecalhoprincipal('ANOTAÇÕES CRIADAS'.center(62))
            for linha_ in arquivo:
                titulo, conteudo = linha_.split(';')
                anotacoes[titulo] = conteudo.strip()

                # Exibe as informaçoes na tela
                print(f'Titulo: {titulo}\nConteúdo: {conteudo}\n')

    except FileNotFoundError:
        print(f'O arquivo {nome} Não foi encontrado.')
    except:
        print('Ocorreu um ERRO ao ler o arquivo.')

    return anotacoes



def criar_notas(arquivo, titulo='Sem Titulo', nota='Sem Nota'):
    try:
        with open(arquivo, 'at') as a:
            a.write(f'{titulo};{nota}\n')
    except FileNotFoundError:
        print(f'O arquivo {arquivo} Não foi encontrado.')
    except:
        print(f'Ocorreu um ERRO ao gravar as anotações.')
    else:
        print(f'Nova nota {titulo} adicionada')


