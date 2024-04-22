print('-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20)
x = float(input('Primeiro segmento: '))
y = float(input('Segundo segmento: '))
z = float(input('Terceiro Segmento: '))
a = x + y
if a > z:
    print('Não é possivel formar um triângulo.')
else:
    print('É possivel formar um triângulo.')
