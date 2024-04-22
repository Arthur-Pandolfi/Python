soma = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    n1, n2 = n2, n1
    
for c in range(n2, n2+1):
    if c % 2 == 0:
        soma += c
print(f'A soma entre os números {n1} e {n2}, considerando todos os números pares em seu intervalo, é {soma}')