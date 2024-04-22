from datetime import date
ano = int(input('Digite algum ano para descobrir se ele é bissexto, se quiser analisar o ano atual, '
                'digite "0":'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é bissexto!')
else:
    print(f'O ano {ano} não é bissexto!')
