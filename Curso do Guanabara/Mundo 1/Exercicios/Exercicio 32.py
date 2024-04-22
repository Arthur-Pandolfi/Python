from datetime import date
ano = int(input('Digite o ano que vocÊ uqer descobrir se é bissexto, digite 0 para analisar o ano'
                ' atual. '))
if ano == 0:
    date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Esse ano é bissexto!')
else:
    print('Esse ano não é bissexto!')