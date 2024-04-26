soma = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        soma += c
    else:
        print(end='')
print(f'O valor da soma de todos os números impares, no intvaelo de 1 a 500 é igual a: {soma}')