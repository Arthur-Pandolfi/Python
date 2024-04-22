from random import choice
real = ['0', '1', '2', '3', '4', '5']
cara = int(input('Digite um número de 0 a 5: '))
z = choice(real)
print(z)
if cara == int(z):
    print('Parábens, você ganhou!')
else:
    print('Você perdeu, tente de novo!')
