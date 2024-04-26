soma = 0
numero = int(input('Digite um número: '))
print('Os divisores desse número é: ')
for c in range(1, numero + 1):
    if numero % c == 0:
        soma += 1
        print(f'\033[32m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end=' ')
if soma >= 3:
    print('\nESSE NÚMERO NÃO È PRIMO')
else:
    print('\nESSE NÚMERO É PRIMO')
    