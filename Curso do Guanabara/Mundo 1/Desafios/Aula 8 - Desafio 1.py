from math import trunc
n = float(input('Digite um número: '))
print('{} Arredondado é igual a {:.0f}'.format(n, n))
# O jeito acima ele só arredonda, e não mostra a parte inteira igual os códigos abaixo
# ----------------------------------------------------------------------------------------------------------------------
print('A parte intera desse número é {}'.format(int(n)))
# ----------------------------------------------------------------------------------------------------------------------
print('A parte inteira desse número é {}'.format(trunc(n)))
