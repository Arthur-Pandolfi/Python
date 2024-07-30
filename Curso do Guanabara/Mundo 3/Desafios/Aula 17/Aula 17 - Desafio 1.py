# listas & Varáveis
numbers = [
    int(input('Digite o primeiro número: ')),
    int(input('Digite o segundo número: ')),
    int(input('Digite o terceiro número: ')),
    int(input('Digite o quarto número: ')),
    int(input('Digite o quinto número: ')),
]
position = 0
largest_number_position = 0
smallest_number_position = 0
largest_number = 0
smallest_number = 458948945456489484899e+4897489894848489

# Códgio
for positon in range(0, len(numbers)):
    #Checa o maior número
    if numbers[position] > largest_number:
        largest_number = numbers[position]
        largest_number_position = position
    
    #Checa o menor número
    if smallest_number > numbers[position]:
        smallest_number = numbers[position]
        smallest_number_position = position

print('-' * 50)
print(f'O maior número encontrado foi o: {largest_number}, na posição {largest_number_position + 1}')
print(f'O menor número encontrado foi o: {smallest_number}, na posição {smallest_number_position + 1}')
