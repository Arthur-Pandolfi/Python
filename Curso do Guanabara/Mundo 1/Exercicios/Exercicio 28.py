from random import randint
from time import sleep
print('\033[1;35m-=-\033[m'*20)
print('\033[1;31mVamos jogar um jogo de adivinhação\033[m?')
sim = input('\033[1;32mSim/Não\033[m ')
print('\033[1;35m-=-\033[m'*20)
capitalizado = sim.capitalize()
computador = randint(0, 5)
if capitalizado == 'Sim':
    print('\033[1;36mOk, vou vou pensar em um número de 0 a 5, e você tem que acertar!\033[m')
    jogador = int(input('\033[1;36mAgora é sua hora de adivinhar! Escreva um número de 0 a 5, e tente adivinhar'
                        'o número que eu pensei!\033[m ')) 
    print('Processando...')
    sleep(3)
    if jogador == computador:
        print('\033[1;33mPoxa, você me venceu! Quer jogar de novo?\033[m')
    else:
        print('\033[1;31mEu ganhei! Vamos jogar de novo?\033[m')

if capitalizado == 'Não':
    print('Ahh, que pena😞! Se você quiser jogar, é só voltar mais tarde!')
