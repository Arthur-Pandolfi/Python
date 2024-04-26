maior = 0
menor = 99999999
for c in range(1, 6):
    peso = int(input(f'Qual o peso de {c}º pessoa? '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(menor, maior)