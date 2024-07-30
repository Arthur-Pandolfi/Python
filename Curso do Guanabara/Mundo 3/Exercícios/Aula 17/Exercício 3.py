# Variaveis
numbers = []
loops = 0
number_quantity = 0
number_to_add = 0.0

# Código Principal
print('Seja bem vindo ao meu programa que organiza os números em ordem crescente sem usar a função sort()!!')
while 5 > loops:
    number_to_add = float(input('Digite um número: '))
    
    if loops == 0:
        numbers.append(number_to_add)
        print('adicionado ao final da lista')
    else:
        number_quantity = len(numbers)
        for x in range(0, number_quantity):
            if numbers[x] > number_to_add:
                numbers.insert(x, number_to_add)
                print(f'o número foi adicionado na posição {x}')
                break
        else:
            numbers.append(number_to_add)
        del(x)
    loops += 1
    
print('Os números em ordem crscente são:',end=' ')
for y in range(0, len(numbers)):
    print(numbers[y], end=' ')