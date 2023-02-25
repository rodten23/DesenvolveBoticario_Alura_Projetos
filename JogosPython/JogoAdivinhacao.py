import Abertura
import Continuacao
import random

def jogar():
    
    Abertura.aber_jogo_adivinhacao()

    print('Temos 3 níveis de dificuldade.\n')
    print('Fácil (F)  -  Médio (M)  -  Difícil (D)\n')

    dificuldade = input('Por favor, digite a letra da dificuldade escolhida: ').upper().strip()

    minimo_tentativas = 4
    tentativas_permitidas = 0
    dificuldade_escolhida = 0

    numero_minimo = 1
    numero_maximo = 100
    numero_secreto = random.randint(numero_minimo,numero_maximo)

    limite_jogo = str(list(range(numero_minimo, numero_maximo + 1))).strip('[]').split(sep=', ')
    
    pontos = 1000

    while(dificuldade != 'F' and dificuldade != 'M' and dificuldade != 'D'):
        print('\nVocê digitou um código de dificuldade inválido.\nPor favor, digite um código F, M ou D para iniciar o jogo.\n')
        dificuldade = input('Por favor, digite a letra da dificuldade escolhida: ').upper().strip()

    if(dificuldade == 'F'):
        tentativas_permitidas = minimo_tentativas + 4
        dificuldade_escolhida = tentativas_permitidas
        print(f'Você tem {dificuldade_escolhida} tentativas.')
    elif(dificuldade == 'M'):
        tentativas_permitidas = minimo_tentativas + 2
        dificuldade_escolhida = tentativas_permitidas
        print(f'Você tem {dificuldade_escolhida} tentativas.')
    elif(dificuldade == 'D'):
        tentativas_permitidas = minimo_tentativas
        dificuldade_escolhida = tentativas_permitidas
        print(f'Você tem {dificuldade_escolhida} tentativas.')

    while(tentativas_permitidas>0):
        
        if(tentativas_permitidas == dificuldade_escolhida):
            print('Espero que acerte de primeira. Boa sorte!\n')
        elif(tentativas_permitidas == dificuldade_escolhida/2):
            print('Não é tão fácil assim, né?\n')
        elif(tentativas_permitidas == 1):
            print('Escolha bem. Essa é sua última tentativa!\n')

        chute_str = input('Digite um número entre {} e {}: '.format(numero_minimo,numero_maximo)).strip()
        
        while (True):
            if (chute_str in limite_jogo):
                break
            else:
                print(f'Desculpe, mas deve digitar um número entre {numero_minimo} e {numero_maximo}!\n')
                chute_str = input('Digite um número entre {} e {}: '.format(numero_minimo,numero_maximo)).strip()
                continue
                
        chute = int(chute_str)
        print('\nVocê escolheu' , chute, '\n')

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto
        pontos_perdidos = 0

        if(acertou):
            print(f'Parabéns, Você Acertou!!!\nTerminou com {pontos} pontos!!!')
            break
        else:
            if(maior):
                print('O seu chute foi maior do que o número secreto!\n')      
            elif(menor):
                print('O seu chute foi menor do que o número secreto!\n')

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        tentativas_permitidas = tentativas_permitidas - 1

    print('O número secreto era {}!!!\n'.format(numero_secreto))

    print('Jogo encerrado!\n')

    Continuacao.continuacao(jogar)

if(__name__ == '__main__'):
    jogar()
