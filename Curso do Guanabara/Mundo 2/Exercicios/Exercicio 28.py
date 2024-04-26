# Variaveis
numero_pa = 0
razao = 0
decimo = numero_pa + (10 - 1) * razao
termos_amais = 0

# Começo
numero_pa = int(input('Digite o número de PA: '))
razao = int(input('Digite a razão: '))
decimo = numero_pa + (10 - 1) * razao

while numero_pa != decimo:
    print(numero_pa, end=' -> ')
    numero_pa += razao
    if numero_pa == decimo:
        print(numero_pa, end=' -> ')
        print('PAUSA', end='')
        termos_amais = int(input('\nQuer ver quantos termos a mais? '))
        numero_pa += termos_amais
        decimo = numero_pa + (termos_amais - 1) * razao
        if termos_amais == 0:
            break
