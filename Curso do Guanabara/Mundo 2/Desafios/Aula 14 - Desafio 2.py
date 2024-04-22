# Importações
from random import randint
from time import sleep

# Variaveis
computador = randint(1, 10)

# Começo
print('\033[1;31mIniciando programa em: \033[m')
sleep(1)
for c in range(3, 0, -1):
    print(f'\033[32m{c}\033[m')
    sleep(1)
print('\033[35m-=-\033[m' * 10)
print('\033[36mJOGO DE ADIVINHAÇÃO\033[m')
print('\033[35m-=-\033[m' * 10)

# Pergunta a opção do usúario:
print('\033[33mEscolha um número de 1 a 10!\033[m')
escolha_pessoa = int(input('\033[36mEu escolho o número: \033[m'))
    # Checa se a pessoa colocou um número maior que 10 ou menor que 0
while escolha_pessoa > 10 or escolha_pessoa < 1:
    print('\033[31mOPÇÃO INVALIDA')
    print('Digite um número valido:\033[m ')
    escolha_pessoa = int(input('\033[36mEu escolho o número: \033[m'))

# Finge que o computador está falando
print('\033[35m-=-\033[m' * 10)
print('\033[33mOk, estou pensando em um número!\033[m')
sleep(2)

# Verifica se a pessoa ganhou ou perdeu
while escolha_pessoa != computador:
    print('TAM TAM TAM')
    sleep(2)
    print('\033[31mVocê perdeu!\033[m')
    print(f'\033[33mEu pensei no número {computador} e você no {escolha_pessoa}!')
    print('\033[35m-=-' * 10)
    print('\033[33mEscolha novamente um número entro 1 e 10!\033[m')
    escolha_pessoa = int(input('\033[36mEu escolho o número: \033[m'))
if escolha_pessoa == computador:
    print('TAM TAM TAM')
    sleep(2)
    print('\033[32mVOCÊ GANHOU!\033[m')
    print(f'\033[33mEu pensei no número {computador}, e você tambem!')
