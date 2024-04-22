# Variaveis
numero = 0
soma = 0
digitados  = 0

# Começo
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
    digitados += 1

print(f'Foi digitado {digitados} números, e a soma de todos eles são: {soma}')