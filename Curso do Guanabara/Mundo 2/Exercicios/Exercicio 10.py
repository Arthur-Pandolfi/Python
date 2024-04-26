from time import sleep
from random import choice
computador_lista = ['Pedra', 'Papel', 'Tesoura']
computador_jogada = choice(computador_lista)
print(computador_jogada)
print('-=-'*12)
print('Seja Bem-Vindo ao JOKENPO do Tutu!')
print('-=-'*12)
print('Escolha sua jogada para coemçar!')
print('''Opções: 
Pedra
Papel
Tesoura''')
print('-'*36)
jogador = str(input(''))
sem_espaco = jogador.strip()
capitalizado = sem_espaco.capitalize()
print('-=-'*12)
if capitalizado == 'Papel' or capitalizado == 'Pedra' or capitalizado == 'Tesoura':
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    if capitalizado == computador_jogada:
        print('Empatamos!')
    elif capitalizado == 'Pedra' and computador_jogada == 'Papel':
        print('Eu ganhei!')
    elif capitalizado == 'Pedra' and computador_jogada == 'Tesoura':
        print('Você ganhou!')
    elif capitalizado == 'Papel' and computador_jogada == 'Tesoura':
        print('Eu ganhei!')
    elif capitalizado == 'Tesoura' and computador_jogada == 'Papel':
        print('Você ganhei!')
    elif computador_jogada == 'Pedra' and capitalizado == 'Papel':
        print('Eu Ganhei!')
    elif computador_jogada == 'Pedra' and capitalizado == 'Tesoura':
        print('Eu ganhei!')
else:
    print('Opção Inválida, tente novamente.')
    sleep(1)
    print('Encerrando programa em')
    sleep(1)
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    print('Programa Encerrado.')
