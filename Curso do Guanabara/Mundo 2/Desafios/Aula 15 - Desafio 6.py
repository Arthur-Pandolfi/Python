from time import sleep

# Variaveis
dinheiro = 0
dinheiro_loop = 0
c50 = 0
c20 = 0
c10 = 0
m1 = 0

# Começo
print('-=-=' * 4)
print(' BANCO DO TUTU')
print('-=-=' * 4)

# Pergunta ao usúario qual o dinheiro que ele quer sacar
dinheiro = int(input('Digite o valor que deseja sacar, em números INTEIROS! \n'))
print('-'*54)
# Faz a checagem de cédulas
while dinheiro_loop != dinheiro:
    # Cédulas de 50
    if dinheiro - dinheiro_loop >= 50:
        dinheiro_loop += 50
        c50 += 1
    # Cédulas de 20
    elif dinheiro - dinheiro_loop >= 20:
        dinheiro_loop += 20
        c20 += 1
    # Cédulas de 10
    elif dinheiro - dinheiro_loop >= 10:
        dinheiro_loop += 10
        c10 += 1
    # Moeda de 1
    else:
        dinheiro_loop += 1
        m1 += 1
# Simula que está processando
print('Processando...')
sleep(3)
print('Processo finalizado.')
print('-'*54)
sleep(0.5)

# Exibe a quantidade de cédulas
print(f'Dinheiro resgatado: {dinheiro_loop}')
print(f'''Cédulas de 50: {c50}
Cédulas de 20: {c20}
Cédulas de 10: {c10}
Moedas de 1: {m1}''')