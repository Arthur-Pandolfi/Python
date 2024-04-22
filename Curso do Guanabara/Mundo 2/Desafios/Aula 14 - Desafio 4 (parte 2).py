numero = int(input('Digite um número: '))
fatorial1 = 1
for c in range(1, numero + 1):
    fatorial = numero
    fatorial1 *= c
print(fatorial1)