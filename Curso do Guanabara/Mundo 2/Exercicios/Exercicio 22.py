media_idade_soma = 0
nome_homem_mais_velho = str('a')
idade_homem_mais_velho = 0
mulheres_20_anos = 0
for c in range(1, 5):
    print(f'-----{c}º Pessoa-----')
    # Capta o Nome, Idade e Sexo das pessoas
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))

    # Media da idade
    media_idade_soma += idade
    media_idade = media_idade_soma / 4

    # Homem mais velho
    if (sexo == 'M' or sexo == 'm') and idade > idade_homem_mais_velho:
        nome_homem_mais_velho = nome
        idade_homem_mais_velho = idade
    
    # Mulheres menores de 20 anos
    if (sexo == 'F' or sexo == 'f') and idade < 20:
        mulheres_20_anos += 1

print(f'A média de idade do grupo é {media_idade}')
print(f'O nome do homem mais velho do grupo é {nome_homem_mais_velho}, e sua idade é {idade_homem_mais_velho}')
print(f'E tem {mulheres_20_anos} mulheres abaixo de 20 anos.')
