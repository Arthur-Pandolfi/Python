# Variaveis
numero_pa = 0
razao = 0
decimo = numero_pa + (10 - 1) * razao

# Começo
numero_pa = int(input('Digite o numero de PA: '))
razao = int(input('Digite a Razão: '))
decimo = numero_pa + (10 - 1) * razao

while numero_pa != decimo:
    numero_pa += razao
    print(numero_pa, end=' ')
print('Acabou')
