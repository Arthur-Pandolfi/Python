from random import randint
computador = randint(1, 10)
vitorias = 0

print('-=-=' * 4)
print('  PAR OU IMPAR')
print('-=-=' * 4)

pessoa = int(input('Digite um número: '))
par_ou_impar = str(input('Par ou Impar? [P/I] ')).capitalize()
total = computador + pessoa
par_ou_impar_final = (total % 2) == 0
print(total)

if par_ou_impar_final == True:
    resposta_certa = 'P'
else:
    resposta_certa = 'I'

while par_ou_impar == resposta_certa:
    vitorias += 1
    if 'I' in resposta_certa:
        print(f'Você jogou {pessoa} e o computador {computador}, e deu Ímpar!\nE você ganhou!')
    elif 'P' in resposta_certa:
        print(f'Você jogou {pessoa} e o computador {computador}, e deu Par!\nE você ganhou!')
    continuar_jogando = input('Quer continuar jogando? [Y/N] ').capitalize()

    if continuar_jogando == 'Y':
        computador += randint(1, 10)
        pessoa = int(input('Digite um número: '))
        par_ou_impar = str(input('Par ou Impar? [P/I] ')).capitalize()
        total = computador + pessoa
        par_ou_impar_final = (total % 2) == 0
        if par_ou_impar_final == True:
            resposta_certa = 'P'
        else:
            resposta_certa = 'I'
    else:
        break

if vitorias == 1:
    print('Game OVER! Você ganhou uma vez!')
if vitorias > 1:
    print(f'Game OVER! Você ganhou {vitorias} vezes!')
if vitorias == 0:
    print('Gamer OVER! Poxa, você não ganhou nenhuma vez...')

