import Abertura
import JogoAdivinhacao
import JogoDaVelha
import JogoForca
import sys

def acessar_menu():

    Abertura.aber_jogo_python()
    
    print('Os jogos disponíveis são:\n')
    print('Adivinhação (1)  -  Jogo da Velha (2)  -  Jogo da Forca (3)  -  Sair (S)\n')

    jogo = input('Qual destes jogos gostaria de iniciar?: ').strip()

    while (jogo != "1" and jogo != "2" and jogo != "3" and jogo != "S" and jogo != "s"):
        jogo = input('\nVocê digitou um código de jogo inválido.\nPor favor, digite 1, 2 ou 3 para iniciar o jogo ou S para Sair: ').strip()

    if (jogo == "1" or jogo == "2" or jogo == "3"):
        escolha = int(jogo) - 1
    else:
        sys.exit('\nObrigado por participar!')

    if(escolha == 0):
        JogoAdivinhacao.jogar()
    elif(escolha == 1):
        JogoDaVelha.jogar()
    elif(escolha == 2):
        JogoForca.jogar()
        
if(__name__ == '__main__'):
    acessar_menu()
