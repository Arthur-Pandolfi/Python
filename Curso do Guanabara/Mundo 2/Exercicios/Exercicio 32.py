soma = 0
digitados = 0
numero = 0

while True:  
    numero = int(input('Digite qualquer número (999 para parar)'))
    if numero == 999:
        break
    else:
        digitados += 1
        soma += numero

print(f'Foram digitados {digitados} números, e a soma de todos eles são: {soma}')