from random import randint

# Tupla & Variáveis
numbers = (
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10),
    randint(1, 10)
         ) 
position = 0

# Código
print('Foi sorteado os números: ',end='')

for position in range(0, len(numbers)):
    print(numbers[position], end=' ')
print()

print(f'Entre eles, o menor número foi o: {min(numbers)}, e o maior foi o: {max(numbers)}')