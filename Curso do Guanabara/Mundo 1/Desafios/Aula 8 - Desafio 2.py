import math
oposto = float(input('Digite o número do cateto oposto: '))
adjancente = float(input('Digite o número do cateto adjancete: '))
hipotenusa = (oposto ** 2 + adjancente ** 2) ** (1/2)
print('O valor de hipotenusa é {:.2f}'.format(hipotenusa))
# ----------------------------------------------------------------------------------------------------------------------
ca = float(input('Digite o valor do cateto adjancete'))
co = float(input('Digite o valor do  cateto oposto'))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:2f}'.format(hi))
