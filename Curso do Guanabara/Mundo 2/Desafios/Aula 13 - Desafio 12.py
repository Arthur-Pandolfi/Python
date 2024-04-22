from datetime import date
ano = date.today().year
pessoas = 0
for c in range(1, 8):
    a = int(input('Digite a data de nascimento: '))
    if ano % a >= 18:
        pessoas += 1
print(f'A qauntidade de pessoas maiores de idade é {pessoas}!')