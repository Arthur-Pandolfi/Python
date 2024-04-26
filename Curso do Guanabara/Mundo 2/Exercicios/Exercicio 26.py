# Variaveis
numero = 0
fatorial = 1
loop = 1

# Começo
numero = int(input('Digite um número: '))

while loop <= numero:
    fatorial *= loop
    loop += 1

print(f'O Fatorial desse número é: {fatorial}')
