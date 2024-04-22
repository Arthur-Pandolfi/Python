num = int(input('Digite um número: '))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        total += c
        print(f'\033[32m{c}\033[m', end=' ')
    else:
        print(f'\033[31m{c}\033[m', end= ' ')
if num + 1 == total:
    print('\n\033[36mO número é primo\033[m')
else:
    print('\n\033[34mO número não é primo\033[m')