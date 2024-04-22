soma = 0
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    n1, n2 = n2, n1
for c in range(n1, n2+1, 2):
    soma += c
print(f'A soma dos números pares do intevalo entre {n1} e {n2} é igual a {soma}')