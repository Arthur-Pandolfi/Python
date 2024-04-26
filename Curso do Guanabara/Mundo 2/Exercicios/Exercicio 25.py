# Variaveis
opcao = 0
numero1 = 0
numero2 = 0
resultado_soma = 0
resultado_multiplicacao = 0
maior_numero = 0

# Começo
print('Escolha uma opção:'
'\n[ 1 ] -> Soma'
'\n[ 2 ] -> Multiplicação'
'\n[ 3 ] -> Maior'
'\n[ 4 ] -> Novos números'
'\n[ 5 ] -> Sair do programa')
print('-' * 30)

# Pergunta a opção do usuario
opcao = int(input(''))

# Pergunta o número pro usuario
numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))

# Novos números
while  opcao == 4:
    print('Digite novamente os números.')
    numero1 = int(input(''))
    numero2 = int(input(''))
    opcao = int(input('Digite uma opção novamente.\n'))

# Soma
if opcao == 1:
    resultado_soma = numero1 + numero2
    print(f'O resultado dessa operação é: {resultado_soma}')

# Multiplicação
if opcao == 2:
    resultado_multiplicacao = numero1 * numero2
    print(f'O resultado dessa operação é: {resultado_multiplicacao}')

# Maior número
if opcao == 3:
    if numero1 > maior_numero:
        maior_numero = numero1

    if numero2 > maior_numero:
        maior_numero = numero2
    print(f'O maior número é o {maior_numero}')

if opcao == 5:
    print('Ok, programa encerrado.')
    exit()