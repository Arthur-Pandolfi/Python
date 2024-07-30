# Listas & Variaveis
numbers = []
numbers_quantity = 0
number_to_add = 0
numbers_sorted = []
five_added = False
continuee = ''
c = 0
x = 0

# Código
while True:
    number_to_add = int(input('Digite o número desejado: '))
    continuee = str(input('Quer continuar? [S/N]')).strip().capitalize()
    numbers_quantity += 1
    numbers.append(number_to_add)
    # Checa se o usuário digitou um valor valido para continuar ou não
    while continuee != 'S' and continuee != 'N':
        continuee = str(input('VOCÊ DIGITOU UM VALOR INVÁLIDO.\nTente novamente\nQuer continuar? [S/N].')).strip().capitalize()
    
    # Checa se o usuárip que continuar
    if continuee == 'N':
        break

# Exibie o resultado para o usuário
print('-=-' * 15)
print()

print(f'Você digitou {numbers_quantity} números')
print()

print('Os números digitados em forma decrescente: ',end='')
numbers_sorted = sorted(numbers)

for c in range(len(numbers_sorted) -1, -1, -1):
   print(numbers_sorted[c], end=' ') 
print()

if 5 in numbers:
    five_added = True
    print(f'O número 5 foi digitado.')
else:
    print(f'O número 5 não foi digitado.')