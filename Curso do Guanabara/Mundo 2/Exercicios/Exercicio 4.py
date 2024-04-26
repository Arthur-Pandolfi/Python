from datetime import date
nasceu = int(input('Você nasceu em que ano? '))
hoje = date.today().year
idade = hoje - nasceu
a = 18 - idade
if idade < 18:
    print(f'Relaxa ainda falta {a} anos para você se alistar!')
elif idade == 18:
    print(f'Ta na hora de você se alistar.')
elif idade > 18:
    print('Ja passo da hora de se alistar ou folgado')