from random import randint
from time import sleep

# Variaveis
computador = randint(0, 10)
jogar = ''
numero_jogador = 0

# Começo
print('\033[36m-=-=\033[m' * 5)
print('\033[32mJogo De Adivinhação!\033[32m')
print('\033[36m-=-=\033[m' * 5)
jogar = input('\033[33mVamos jogar um jogo? [Y/N]\033[m ').capitalize()
print('-'*23)


if jogar == 'Y':
    print('\033[32mOk, começando o jogo...\033[m')
    print('\033[34mPara começar, eu vou pensar em um número, e você em outro!\033[m')
    numero_jogador = int(input('\033[33mDigite um número entre 0 e 10! \033[m'))

    while  numero_jogador < 0 or numero_jogador > 10:
        print('\033[33mVocê digitou um número invalido! Digite um número valido para continuar.')
        numero_jogador = int(input('\033[34mDigite outro número:\033[34m '))
    
    while numero_jogador != computador:
        print('\033[31mVocê perdeu!\033[m \033[34mDigite outro número e tente ganhar de mim!\033[m')
        numero_jogador = int(input('\033[33mDigite um número entre 0 e 10! \033[m'))

    print('\033[34mParabéns! Você\033[m\033[32m ganhou\033[m\033[34m!\033[m')
    
else:
    print('\033[31mOk, encerrando o programa...\033[m')
    for c in range(3, 0, -1):
        print(c)
        sleep(1)
    print('Programa encerrado.')