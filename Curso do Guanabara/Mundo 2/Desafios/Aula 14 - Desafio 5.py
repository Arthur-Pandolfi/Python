# Variaveis
numero_pa = 0
razao = 0
decimo = numero_pa + (10 - 1) * razao

# Começo
numero_pa = int(input('Digite um número: '))
razao = int(input('Qual a razão? '))
decimo = numero_pa + (10 - 1) * razao

# Meio
    # Começo do loop
while numero_pa != decimo:
    numero_pa += razao
    print(numero_pa, end=' ')
print('\nACABOU')