def leiaint(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: Por favor, digite um numero inteiro valido.\033[0m')
        except KeyboardInterrupt:
            print('O usuário decidiu não informar mais o número.')
            return 0
        else:
            return inteiro


def linha(tam=62):
    print('-' * tam)


def cabecalhoprincipal(txt):
    print('=' * 62)
    print(txt.center(62))
    print('=' * 62)


def cabecalhosecundario(txt):
    print('¬' * 62)
    print(txt.center(62))
    print('¬' * 62)


def menu(lista):
    cabecalhosecundario('\033[34mMENU PRINCIPAL\033[0m')
    contador = 1
    for item in lista:
        print(f'\033[33m{contador}\033[0m - \033[34m{item}\033[0m')
        contador += 1
    print(linha())
    opcao = leiaint('\033[32mSua opção:\033[0m')
    return opcao
