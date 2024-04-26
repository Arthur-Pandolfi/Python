# Variaveis
numero = 0
numeros_digitados = 0
soma = 0

# Começo
while numero != 999:
    numero = int(input('Digite um número: '))
    numeros_digitados += 1
    soma += numero
print(f'Foi digitado {numeros_digitados - 1} números, e a soma de todos os valores é {soma - 999}')