# Variaveis
soma = 0
multiplicacao = 0
maior = 0

# Começo
numero_1 = int(input('Digite um número: '))
numero_2 = int(input('Digite outro número: '))
print('-' * 25)
print('''Escola alguma opção:
[ 1 ] -> Somar
[ 2 ] -> Multiplicar
[ 3 ] -> Maior número
[ 4 ] -> Novos números 
[ 5 ] -> Sair do programa''')
print('-' * 25)
escolha_operação = int(input(''))

# Operações

# Coloca o While para a opção 4
while escolha_operação == 4:
    numero_1 = int(input('Digite um número: '))
    numero_2 = int(input('Digite outro número: '))
    print('-' * 25)
    print('''Escola alguma opção:
[ 1 ] -> Somar
[ 2 ] -> Multiplicar
[ 3 ] -> Maior número
[ 4 ] -> Novos números 
[ 5 ] -> Sair do programa''')
    print('-' * 25)
    escolha_operação = int(input(''))
if escolha_operação == 1:
    soma = (numero_1 + numero_2)
    print(f'O resultado dessa soma é: {soma}')

if escolha_operação == 2:
    multiplicacao = (numero_1 * numero_2)
    print(f'O resultado dessa operação é: {multiplicacao}')

if escolha_operação == 3:
    if numero_1 > numero_2:
        maior = numero_1
        print(f'O maior número é o primeiro ({maior})')
    elif numero_2 > numero_1:
        maior = numero_2
        print(f'O maior número é o segundo ({maior})')

if escolha_operação == 5:
    pass