frase = str(input('DIgite uma frase: '))
minusculo = frase.lower()
separado = frase.split()
junto = ''.join(separado)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]

junto_capitalizado = frase.capitalize()
inverso_capitalizado = inverso.capitalize()

print(f'Normal: {junto_capitalizado}\n'
    f'Inverso: {inverso_capitalizado}\n')
if inverso_capitalizado == junto_capitalizado:
    print('ESSA FRASE È UM PALINDROMO')
else:
    print('ESSA FRASE NÃO È UM PALINDROMO')