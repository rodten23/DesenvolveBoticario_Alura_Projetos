import Continuacao
import random

def jogar():
    print('\n*********************************')
    print('***Bem vindo ao Jogo da Forca!***')
    print('*********************************\n')

    palavra_secreta = 'cocada'.upper()

    letras_acertadas = ['_' for letra in palavra_secreta]

    print(letras_acertadas)

    enforcou = False
    acertou = False

    erros = 0

    while(not enforcou and not acertou):

        chute = input('\nQual letra? ').upper().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra.upper()
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Mas ainda tem {6-erros} tentativas.")

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print('Você ganhou!')
    else:
        print('Você perdeu!')
              
    print('Jogo encerrado!\n')

    Continuacao.continuacao(jogar)

if(__name__ == '__main__'):
    jogar()