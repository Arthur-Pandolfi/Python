# Variaveis
numero = 0
fatorial = 1
loop = 1    

# Começo
    # Pergunta o número ao usuario
numero = int(input('Digite um número: '))

# Fim
    # Começa o loop
while loop <= numero:
    fatorial *= loop
    loop += 1

print(f'O fatorial do número {numero}, é {fatorial}')
