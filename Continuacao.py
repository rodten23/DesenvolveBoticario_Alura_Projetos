import JogosEmPython
import sys

def continuacao(jogar):
    while(True):

        print('\nAgora, você gostaria de:\n')

        print('Jogar novamente (N)  -  Voltar para o menu (V)  -  Sair (S)\n')

        continua = input('Por favor, digite N, V ou S: ').upper().strip()

        while(continua != 'N' and continua != 'V' and continua != 'S'):
            print('Você digitou um código inválido.\n')
            continua = input('Por favor, digite N, V ou S: ').upper().strip()

        if(continua == 'N'):
            jogar()
        elif(continua == 'V'):
            JogosEmPython.acessar_menu()
        elif(continua == 'S'):
            sys.exit('\nObrigado por participar!')