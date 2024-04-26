# Variaveis
numero = 0
continuar = ''
media_soma = 0
media_contagem = 0
media = 0
menor = float('inf')
maior = 0

# Começo
while continuar != 'N':
    numero = int(input('Digite um número:'))
    media_soma += numero
    media_contagem += 1
    if menor > numero:
        menor = numero
    if numero > maior:
        maior = numero
    continuar = str(input('Quer continuar a digitar números? [Y/N]')).capitalize()
    while continuar != 'Y' and  continuar != 'N':
        print('Valor invalido, digite algo correto.')
        continuar = str(input('Quer continuar a digitar números? [Y/N]')).capitalize()
media = media_soma / media_contagem
print(f'O maior número é o {maior}, o menor é o {menor}, e a média é {media}')
