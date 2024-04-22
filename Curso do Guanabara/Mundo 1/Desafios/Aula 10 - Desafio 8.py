x = float(input('Digite o comprimento de uma reta: '))
y = float(input('DIgite o comprimento de outra reta: '))
z = float(input('Digite o comprimento de outra reta: '))
reta1 = x + y
if reta1 > z:
    print('Essas medidas não formam um triangulo.')
else:
    print('Essas medidas formam um triangulo.')

