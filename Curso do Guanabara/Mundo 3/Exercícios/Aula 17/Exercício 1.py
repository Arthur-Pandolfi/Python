# Variaveis usadas
numbers = []
max_numbers_position = []
min_numbers_position = []
numer = int
max_number = 0
min_number = float('inf')
position = int

# Código principal
print('Seja bem vindo ao meu programa de descobrir o maior valor da lista!')

for i in range(0, 5):
    print(f'Posição {i}:', end=' ')
    number = int(input(''))
    numbers.append(number)

for position in range(len(numbers)):
    if numbers[position] > max_number:
        max_number = numbers[position]
        max_numbers_position = []
    if numbers[position] == max_number:
        max_numbers_position.append(position)
    if min_number > numbers[position]:
        min_number = numbers[position]
        min_numbers_position = []
    if min_number == numbers[position]:
        min_numbers_position.append(position)

print(f'O maior número encontrado foi o: {max_number}, que apareceu nas posições:', end=' ')
for x in range(0, len(max_numbers_position)):
    print(max_numbers_position[x], end=' ')
print()
print(f'Já, o menor número encontrado foi o: {min_number}, que apareceu nas posições:', end=' ')
for z in range(0, len(min_numbers_position)):
    print(min_numbers_position[z], end=' ')
