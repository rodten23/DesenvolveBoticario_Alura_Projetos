import Continuacao
import random

def recepcao_forca():

    print('\n*********************************')
    print('***Bem vindo ao Jogo da Forca!***')
    print('*********************************\n')

def carrega_palavra_sorteada():

    palavras = []

    with open('Palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_sorteada = palavras[random.randint(0,len(palavras))].upper()

    return palavra_sorteada

def oculta_letras(palavra_sorteada):
    return ['_' for letra in palavra_sorteada]

def jogar():

    recepcao_forca()

    palavra_secreta = carrega_palavra_sorteada()

    letras_acertadas = oculta_letras(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input('\nQual letra? ').upper().strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra.upper()
                index += 1
        else:
            erros += 1
            print(f"Ops, você errou! Mas ainda tem {6-erros} tentativas.\n")

        enforcou = erros == 6
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        print('\nVocê ganhou!\n')
    else:
        print('Você perdeu!\n')
        print(f'A palavra secreta era {palavra_secreta}!\n')
              
    print('Jogo encerrado!')

    Continuacao.continuacao(jogar)

if(__name__ == '__main__'):
    jogar()