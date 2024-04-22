from math import hypot
adjancente = float(input('Digite o valor do cateto Adjancente: '))
oposto = float(input('Digite o valor do cateto Oposto: '))
hipottenusa = hypot(oposto, adjancente)
print(f'o valor de hipotenusa é {hipottenusa:.2f}')
