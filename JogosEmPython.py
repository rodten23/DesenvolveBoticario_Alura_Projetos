import JogoAdivinhacao
import JogoDaVelha
import JogoForca

print('\n********* JOGOS * PYTHON *********')
print('******** Sejam Bem Vindos ********')
print('***** Que a diversão comece! *****\n')

print('Os jogos disponíveis são:\n')
print('(1) Adivinhação   (2) Jogo da Velha   (3) Jogo da Forca\n')

jogo = input('Qual destes jogos gostaria de iniciar?: ')

while (jogo != "1" and jogo != "2" and jogo != "3"):
    jogo = input('\nVocê digitou um código de jogo inválido.\nPor favor, digite 1, 2 ou 3 para iniciar o jogo: ')

escolha = int(jogo)

if(escolha == 1):
    JogoAdivinhacao.jogar()
elif(escolha == 2):
    JogoDaVelha.jogar()
elif(escolha == 3):
    JogoForca.jogar()

