from datetime import date
nasceu = int(input('Em que ano você nasceu? '))
hoje = date.today().year
idade = hoje - nasceu
if idade <= 9 or idade == 9:
    print(f'Você participara da categoria MIRIM')
elif idade <= 14 or idade == 14:
    print(f'Você participara da categoria INFANTIL')
elif idade <= 19 or idade == 19:
    print(f'Você participara da categoria JUNIOR')
elif idade <= 25 or idade == 25:
    print(f'Você participara da categoria SÊNIOR')
else:
    print(f'Você participara da categoria MASTER')