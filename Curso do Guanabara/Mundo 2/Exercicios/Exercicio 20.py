from datetime import date

data = date.today().year
soma_menor = 0
soma_maior = 0

for c in range(1, 8):
    idade = int(input('Em que ano a 1º pessoa nasceu? '))
    if data - idade >=18:
        soma_maior += 1
    if data - idade <=18:
        soma_menor += 1

if soma_maior == 1:
    print(f'Tem apenas 1 pessoa menor de idade no grupo')
if soma_maior == 2:
    print(f'Tem 2 pessoas maiores de idade neste grupo')
if soma_maior == 3:
    print(f'Tem 3 pessoas maiores de idade neste grupo')
if soma_maior == 4:
    print(f'Tem 4 pessoas maiores de idade neste grupo')
if soma_maior == 5:
    print(f'Tem 5 pessoas maiores de idade neste grupo')
if soma_maior == 6:
    print(f'Tem 6 pessoas maiores de idade neste grupo')
if soma_maior == 7:
    print(f'Tem 7 pessoas maiores de idade neste grupo')