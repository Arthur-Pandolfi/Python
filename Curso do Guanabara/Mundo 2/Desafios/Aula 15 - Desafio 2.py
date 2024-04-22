# Variaveis
numero = 0
tabuada = 1
jafoimultiplicado = 0

# Começo
while True:
    if jafoimultiplicado == 0:
        numero = int(input('DIGITE UM NUMERO NEGATIVO PARA PARAR\nDigite um número que deseja ver a tabuada: '))
        jafoimultiplicado += 1
    else:
        numero = int(input('\nDIGITE UM NUMERO NEGATIVO PARA PARAR\nDigite um número que deseja ver a tabuada: '))
    if numero < 0:
        break
    for tabuada in range(1, 11):
        print(numero * tabuada, end=' ')