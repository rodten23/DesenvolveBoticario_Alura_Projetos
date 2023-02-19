import random

def jogar():
    print('\n*********************************')
    print('***Bem vindo ao Jogo da Velha!***')
    print('*********************************\n')

    posicoes = ['1','2','3',
                '4','5','6',
                '7','8','9']
    
    tabuleiro = ['-','-','-',
                 '-','-','-',
                 '-','-','-']

    def apresentar_tabuleiro(marcacoes):
        print(f'\n {marcacoes[0]} | {marcacoes[1]} | {marcacoes[2]}')
        print(' - - - - -')
        print(f' {marcacoes[3]} | {marcacoes[4]} | {marcacoes[5]}')
        print(' - - - - -')
        print(f' {marcacoes[6]} | {marcacoes[7]} | {marcacoes[8]}')

    print('Você pode jogar em dupla ou contra o computador.\n')
    print('Dupla (D)  -  Contra Computador (C)\n')

    modo_jogo = input('Por favor, digite a letra do modo escolhido: ').upper()

    while(modo_jogo != 'D' and modo_jogo != 'C'):
        print('Você digitou um modo inválido.\nPor favor, digite um código D ou C para iniciar o jogo.\n')
        modo_jogo = input('Por favor, digite a letra do modo escolhido: ').upper()

    print('\nEstas são as posições no tabuleiro.')

    apresentar_tabuleiro(posicoes)

    jogador_x = 'X'
    jogador_o = 'O'

    def jogada_dupla(tabuleiro, jogador):
        print(f'\nAgora é a vez do jogador {jogador}.')
        posicao = int(input('Realize sua jogada digitando uma posição de 1 a 9: ')) - 1
        while(posicao<0 or posicao>8 or tabuleiro[posicao] != '-'):
            print('Jogada inválida!')
            posicao = int(input('Realize sua jogada digitando uma posição de 1 a 9: ')) - 1
        tabuleiro[posicao] = jogador

    def jogada_computador(tabuleiro, jogador):
        if(jogador == jogador_x):
            print(f'\nAgora é a sua vez marcando X.')
            posicao = int(input('Realize sua jogada digitando uma posição de 1 a 9: ')) - 1
            while(posicao<0 or posicao>8 or tabuleiro[posicao] != '-'):
                print('Jogada inválida!')
                posicao = int(input('Realize sua jogada digitando uma posição de 1 a 9: ')) - 1
            tabuleiro[posicao] = jogador
        elif(jogador == jogador_o):
            print(f'\nComputador jogou marcando O.')
            jogada_computador = random.randint(0,8)
            while(tabuleiro[jogada_computador] != '-'):
                jogada_computador = random.randint(0,8)
            tabuleiro[jogada_computador] = jogador

    def checar_vitoria_horizontal(tabuleiro, jogador):
        if(tabuleiro[0] == jogador and tabuleiro[1] == jogador and tabuleiro[2] == jogador) or \
            (tabuleiro[3] == jogador and tabuleiro[4] == jogador and tabuleiro[5] == jogador) or \
            (tabuleiro[6] == jogador and tabuleiro[7] == jogador and tabuleiro[8] == jogador):
            return True
        else:
            return False
        
    def checar_vitoria_vertical(tabuleiro, jogador):
        if(tabuleiro[0] == jogador and tabuleiro[3] == jogador and tabuleiro[6] == jogador) or \
            (tabuleiro[1] == jogador and tabuleiro[4] == jogador and tabuleiro[7] == jogador) or \
            (tabuleiro[2] == jogador and tabuleiro[5] == jogador and tabuleiro[8] == jogador):
            return True
        else:
            return False
        
    def checar_vitoria_diagonal(tabuleiro, jogador):
        if(tabuleiro[0] == jogador and tabuleiro[4] == jogador and tabuleiro[8] == jogador) or \
            (tabuleiro[2] == jogador and tabuleiro[4] == jogador and tabuleiro[6] == jogador):
            return True
        else:
            return False
        
    def checar_empate(tabuleiro):
        if('-' in tabuleiro):
            return False
        else:
            print('\nJogo Empatou!')
            return True
        
    def checar_vitoria(tabuleiro, jogador):
        if(checar_vitoria_horizontal(tabuleiro, jogador) or \
            checar_vitoria_vertical(tabuleiro, jogador) or \
            checar_vitoria_diagonal(tabuleiro, jogador)):
            if(modo_jogo == 'D'):
                print(f'\nJogador {jogador} é o Vencedor!')
                return True
            elif(modo_jogo == 'C'):
                if(jogador == jogador_x):
                    print(f'\nVocê Venceu!')
                    return True
                elif(jogador == jogador_o):
                    print(f'\nVocê Perdeu!')
                    return True
        else:
            return False

    if(modo_jogo == 'C'):
        while(True):
            jogada_computador(tabuleiro, jogador_x)
            apresentar_tabuleiro(tabuleiro)
            if(checar_vitoria(tabuleiro, jogador_x) or checar_empate(tabuleiro)):
                break
            
            jogada_computador(tabuleiro, jogador_o)
            apresentar_tabuleiro(tabuleiro)
            if(checar_vitoria(tabuleiro, jogador_o) or checar_empate(tabuleiro)):
                break
        
    elif(modo_jogo == 'D'):
        while(True):
            jogada_dupla(tabuleiro, jogador_x)
            apresentar_tabuleiro(tabuleiro)
            if(checar_vitoria(tabuleiro, jogador_x) or checar_empate(tabuleiro)):
                break
            
            jogada_dupla(tabuleiro, jogador_o)
            apresentar_tabuleiro(tabuleiro)
            if(checar_vitoria(tabuleiro, jogador_o) or checar_empate(tabuleiro)):
                break
        
    print("\nJogo encerrado! Obrigado por participar!\n")

if(__name__ == '__main__'):
    jogar()