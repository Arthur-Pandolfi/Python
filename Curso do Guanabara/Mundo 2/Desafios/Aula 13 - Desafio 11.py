frase = str(input('Digite uma frase: '))
minusculo = frase.lower()
palavras = minusculo.split()
palavras_juntas = ''.join(palavras)
inverso = ''

for letra in range(len(palavras_juntas) -1, -1, -1):
    inverso += palavras_juntas[letra]

maiuscula_normal = frase.capitalize()
maiuscula_inverso = frase.capitalize()

print(f'Normal: {maiuscula_normal} \n'
     f'Reverso: {maiuscula_inverso}')

if inverso == palavras_juntas:
    print('Essa frase é um palindromo!')
else:
    print('Não é um palindromo!')
