# Variaveis
numero = 0
soma = 0

# Começo

numero = int(input('Digite um número: '))

# Fim

while numero != 999:
    soma += numero
    numero = int(input('Digite outro numero: '))
# Checa se o número é igual a 999
if numero == 999:
    print(f'A soma entre esses números foi: {soma}')