from math import inf

# Variaveis
continuar = 'a'
numero_escolhido = 0
soma = 0
quantidade_de_valores_media = 0
media = 0
maior = 0
menor = inf

# Começo
while continuar != 'N':
    numero_escolhido = int(input('Digite um número: '))
    soma += numero_escolhido
    quantidade_de_valores_media += 1
    if numero_escolhido > maior:
        maior = numero_escolhido
    if numero_escolhido < menor:
        menor = numero_escolhido
    if quantidade_de_valores_media >= 2:
        print('Quer continuar digitando números? [Y/N]', end='')
        continuar = str(input('')).capitalize()

media = soma / quantidade_de_valores_media

# Fim
print(f'A soma entre todos os números digitados é {soma}, a média é {media}, o maior é {maior}, o menor é {menor}'
      f', e a quantidade de números digitados foram {quantidade_de_valores_media}')