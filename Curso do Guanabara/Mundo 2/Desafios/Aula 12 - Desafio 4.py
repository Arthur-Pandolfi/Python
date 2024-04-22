from datetime import date
idade = int(input('Em que ano você nasceu? '))
hoje = date.today().year - idade
anos = hoje - 18
if hoje < int('18'):
    print(f'Fica tranquilo, ainda falta {anos} para se alistar!')
elif hoje == int('18'):
    print(f'Ferro, ta na sua vez de se alistar😞')
else:
    print(f'Ja passo da hora de se alistar em, folgado! Você está {anos} anos atrasados!')
    
