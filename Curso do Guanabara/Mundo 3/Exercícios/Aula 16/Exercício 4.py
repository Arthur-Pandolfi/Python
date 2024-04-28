# Váriaveis & Tuplas
numbers = (
    int(input('Digite um número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o quarto número: '))
          )
position = 0
quantity_of_9 = 0
first_3_position = 999
pair_numbers_quantity = 0

# Código
print('-=-' * 32)

#Checa a quantidade de 9 que apareceu
for position in range(0, len(numbers)):
    if numbers[position] == 9:
        quantity_of_9 += 1
position = 0

#Primeira posição do número 3
for position in range(0, len(numbers)):
    if numbers[position] == 3:
        first_3_position = position
        break
position = 0

#Quais foram os números pares
for position in range(0, len(numbers)):
    if (numbers[position] % 2) == 0:
        pair_numbers_quantity += 1
position = 0

# Exibe ao usuário o resultado
if quantity_of_9  == 0:
    print('Você não digitou nenhum número 9.')

else:
    print(f'Você digitou {quantity_of_9} números 9.')

if first_3_position == 999:
    print('Não apareceu nenhum número 3.')

else:
    print(f'O primeiro número 3 apareceu na posição: {first_3_position + 1}')

if pair_numbers_quantity == 0:
    print('Não foi digitado nenhum número par.')

else:
    print(f'Foi digitado {pair_numbers_quantity} números pares.')
