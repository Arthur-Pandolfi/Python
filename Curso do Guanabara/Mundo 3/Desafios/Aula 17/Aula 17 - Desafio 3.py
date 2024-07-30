# Lista & Varáveis
numbers = []
position = 1
number_to_add = 0
numbers_quantity = 0

# Código
while True:
    if numbers_quantity == 5:
        break
    
    number_to_add = int(input('Digite um número: '))
    if numbers_quantity == 0:
        numbers.append(number_to_add)
        
    else:
        for position in range(0, len(numbers)):
            if numbers[position] > number_to_add:
                numbers.insert(position, number_to_add)
                break
    numbers_quantity += 1

# Exibie o resultado
for c in range(0, len(numbers)):
    print(numbers[c], end=' ')