print('\033[1;35m-=-\033[m'*20)
num = int(input('Digite um número inteiro: '))
a = int(input("""[ 1 ] para Binário
[ 2 ] para Octal
[ 3 ] para Hexadecimal
  """))
print('\033[1;35m-=-\033[m'*20)
if a == int('1'):
    print('O valor {} em Binário é igual a {:b}!'.format(num,num))
elif a == int('2'):
    print('O valor {} em Octal é igual a {:o}!'.format(num,num))
elif a == int('3'):
    print('O valor {} em Hexa-Decimal é {:x}!'.format(num,num))
elif a != int('1') and a != int('2') and a != int('3'):
    print(f'Valor Inválido.')