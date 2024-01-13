from time import sleep

from lib.funcoes import *

arquivo = 'notas.txt'

if not arquivo_existente(arquivo):
    criar_arquivo(arquivo)

while True:
    cabecalhoprincipal('\033[33mHÓRUS-PAD V-0.1.1\033[0m')
    resposta = menu(['VER NOTAS CRIADAS', 'CRIAR UMA NOVA NOTA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        # Mostrar todas as notas criadas
        lerarquivo(arquivo)
    elif resposta == 2:
        # Cria uma nova nota
        cabecalhoprincipal('CRIANDO UMA NOVA ANOTAÇÃO'.center(62))
        titulo = str(input('Informe o titulo: '))
        nota = str(input('Escreva a nota: '))
        criar_notas(arquivo, titulo, nota)
    elif resposta == 3:
        cabecalhosecundario('\033[36mSaindo do sistema... Até logo!\033[0m')
        break
    else:
        # Digitou uma opção incorreta no menu
        cabecalhosecundario('\033[31mERRO!: Digite uma opção válida!\033[0m')
    sleep(1)
