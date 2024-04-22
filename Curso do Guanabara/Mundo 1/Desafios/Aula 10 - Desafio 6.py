n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
# Verificando o menor
menor = n1
if n1 > n2 and n2 < n3:
    menor = n2
if n3 < n1 and n2 > n3:
    menor = n3
# Verificando o maior
maior = n1
if n2 > n1 and n3 < n2:
    maior = n2
if n3 > n2 and n1 < n3:
    maior = n3
print(f'O maior número é {maior}\nO menor número é {menor}')
