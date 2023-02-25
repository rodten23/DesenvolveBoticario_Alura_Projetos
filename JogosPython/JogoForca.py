import Abertura
import Continuacao
import random

def carrega_palavra_sorteada():

    palavras = []

    with open('Palavras.txt', 'r') as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_sorteada = palavras[random.randint(0,len(palavras))].upper()

    return palavra_sorteada

def oculta_letras(palavra_sorteada):
    return ['_' for letra in palavra_sorteada]

def marca_chute_correto(chute, palava_secreta, letras_acertadas):
    index = 0
    for letra in palava_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra.upper()
        index += 1

def pede_outra_letra(chute):
    print(f'\nLetra {chute} já foi. Agora, escolha outra letra.')

def desenha_forca(erros):
    print('  _______     ')
    print(' |/      |    ')

    if(erros == 1):
        print(' |      (_)   ')
        print(' |            ')
        print(' |            ')
        print(' |            ')

    if(erros == 2):
        print(' |      (_)   ')
        print(' |      \     ')
        print(' |            ')
        print(' |            ')

    if(erros == 3):
        print(' |      (_)   ')
        print(' |      \|    ')
        print(' |            ')
        print(' |            ')

    if(erros == 4):
        print(' |      (_)   ')
        print(' |      \|/   ')
        print(' |            ')
        print(' |            ')

    if(erros == 5):
        print(' |      (_)   ')
        print(' |      \|/   ')
        print(' |       |    ')
        print(' |            ')

    if(erros == 6):
        print(' |      (_)   ')
        print(' |      \|/   ')
        print(' |       |    ')
        print(' |      /     ')

    if (erros == 7):
        print(' |      (_)   ')
        print(' |      \|/   ')
        print(' |       |    ')
        print(' |      / \   ')

    print(' |            ')
    print('_|___         \n')

def confirma_vitoria():
    print('\nParabéns!!! Você ganhou!!!\n')

    print('       ___________      ')
    print('      "._==_==_=_."     ')
    print('      .-\\:      /-.    ')
    print('     | (|:.     |) |    ')
    print('      "-|:.     |-"     ')
    print('        \\::.    /      ')
    print('         "::. ."        ')
    print('           ) (          ')
    print('         _.' '._        ')
    print('        "-------"       ')

    print('\n    Jogo encerrado!\n')

def confirma_derrota(palavra_secreta):
    print('\nPuxa, infelizmente você perdeu!\n')
    print(f'A palavra secreta era {palavra_secreta}!\n')
    
    print('    _______________         ')
    print('   /               \       ')
    print('  /                 \      ')
    print('//                   \/\  ')
    print('\|   XXXX     XXXX   | /   ')
    print(' |   XXXX     XXXX   |/     ')
    print(' |   XXX       XXX   |      ')
    print(' |                   |      ')
    print(' \__      XXX      __/     ')
    print('   |\     XXX     /|       ')
    print('   | |           | |        ')
    print('   | I I I I I I I |        ')
    print('   |  I I I I I I  |        ')
    print('   \_             _/       ')
    print('     \_         _/         ')
    print('       \_______/           ')

    print('\n    Jogo encerrado!\n')

def jogar():

    Abertura.aber_jogo_forca()

    palavra_secreta = carrega_palavra_sorteada()

    letras_acertadas = oculta_letras(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input('\nQual letra? ').upper().strip()

        if(chute in letras_acertadas):
            pede_outra_letra(chute)
            continue
        elif(chute in palavra_secreta):
            marca_chute_correto(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            print(f'Ops, você errou! Mas ainda tem {6-erros} tentativas.\n')

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

        print(f'\n{letras_acertadas}')

    if(acertou):
        confirma_vitoria()
    else:
        confirma_derrota(palavra_secreta)

    Continuacao.continuacao(jogar)

if(__name__ == '__main__'):
    jogar()