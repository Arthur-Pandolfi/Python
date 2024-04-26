num = int(input('Digite um número inteiro: '))
a = int(input('''[ 1 ] Para BINARIO
[ 2 ] Para OCTAL
[ 3 ] Para HEXA-DECIMAL
  '''))
if a == int('1'):
    print('O valor {} em números binários é igual a {:b}'.format(num,num))
elif a == int('2'):
    print('O valor {} em octal é igual a {:o}'.format(num,num))
if a == int('3'):
    b = str(input('Você quer em letras Maiusculas ou Minusculas? '))
    capitalizado = b.capitalize()
    if capitalizado == 'Maiusculas':
        print('O número {} em Hexa-Decimal com letras Maiusculas é igual a {:X}'.format(num,num))
    if capitalizado == 'Minusculas':
        print('O número {} em Hexa-Decimal com letras Minusculas é igual a {:x}'.format(num,num))
