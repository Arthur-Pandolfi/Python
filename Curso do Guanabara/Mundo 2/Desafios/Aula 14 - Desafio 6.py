# Variaveis
numero_pa = 0
razao = 0
termos_amais = 0
decimo = numero_pa + (10 - 1) * razao

# Começo
numero_pa = int(input('Digite um número: '))
razao = int(input('Digite a razão: '))
decimo = numero_pa + (11 - 1) * razao

# Fim

# Começa o loop
while numero_pa != decimo:
    print(numero_pa, end=' -> ')
    numero_pa += razao
    if numero_pa == decimo:
        print('PAUSA')
    while numero_pa >= decimo:
        termos_amais = int(input('Quantos termos a mais? '))
        if termos_amais == 0:
            exit()
        decimo = numero_pa + (termos_amais - 1) * razao
        print(numero_pa, end=' -> ')
        numero_pa += razao
        if numero_pa >= decimo:
            print(decimo)
