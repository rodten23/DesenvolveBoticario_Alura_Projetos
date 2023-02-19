import JogoAdivinhacao
import JogoDaVelha
import JogoForca

print('\n********* JOGOS * PYTHON *********')
print('******** Sejam Bem Vindos ********')
print('***** Que a diversão comece! *****\n')

print('Os jogos disponíveis são:\n')
print('(1) Adivinhação   (2) Jogo da Velha   (3) Jogo da Forca\n')

jogo = int(input('Qual destes jogos gostaria de iniciar?: '))

if(jogo == 1):
    JogoAdivinhacao.jogar()
elif(jogo == 2):
    JogoDaVelha.jogar()
elif(jogo == 3):
    JogoForca.jogar()

