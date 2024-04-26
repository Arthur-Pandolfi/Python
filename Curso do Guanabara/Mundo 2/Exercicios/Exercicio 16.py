soma = 0
for c in range(1, 7):
    numero = int(input(f'Digite {c}º número: '))
    if numero % 2 == 0:
        soma += numero
print(f'O resultado da soma de todos os números pares nesse intervalo é: {soma}')