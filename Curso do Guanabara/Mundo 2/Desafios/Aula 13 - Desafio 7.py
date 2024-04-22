soma = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
for c in range(n1, n2 + 1):
    if c % 2 == 0:
        soma += c
print(f'A soma de todos números pares do intervalo entre {n1} e {n2} é {soma}!')