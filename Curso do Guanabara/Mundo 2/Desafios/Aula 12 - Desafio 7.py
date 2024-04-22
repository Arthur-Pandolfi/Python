x = float(input('Digite o valor da primeira reta: '))
y = float(input('Digite o valor da segunda reta: '))
z = float(input('Digite o valor da terceira reta: '))
print('-'*50)
a = x + y
triangulo = a > z
if triangulo == False:
    print(f'Esse valor forma um \033[1;35mTriangulo\033[m!')
if triangulo == True:
    print(f'Esse valor não forma um \033[1;35mTriângulo\033[m')
if x == y and z == x and z == y:
    print(f'Esse triangulo é \033[1;34mEquilátero\033[m!')
elif x != y and x != z and y != z:
    print(f'Esse triangulo é \033[1;36mEscaleno\033[m!')
else:
    print(f'Esse triângulo é \033[1;32mIsóceles\033[m!')
