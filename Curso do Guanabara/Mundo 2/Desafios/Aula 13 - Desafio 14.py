tem_so_homems = str(input('Tem só homems? '))
capitalizado1 = tem_so_homems.capitalize()
replacado1 = str('a')
quantidade_menor_de_20 = 0
media_idade_soma = 0
media_idade = 0
nome_homem_mais_velho = str('')
idade_homem_mais_velho = 0
if capitalizado1 == 'Nao':
    replacado1 = capitalizado1.replace('Nao', 'Não')
if replacado1 == str('Não'):
    tem_so_mulheres = str(input('Tem só mulheres? '))
    capitalizado2 = tem_so_mulheres.capitalize()
    capitalizado3 = tem_so_mulheres.capitalize()
    replacado2 = capitalizado3.replace('Nao', 'Não')
    if replacado2 == 'Não':
        ambos = str(input('Então tem ambos? '))
        capitalizado4 = ambos.capitalize()
        if capitalizado4 == str('Sim'):
            print('Primeiro virá os homens do grupo')
            for c in range(1,3):
                nome = str(input('Qual o nome? '))
                idade = int(input('Qual idade? '))
                media_idade_soma += idade
                if c == 1 or idade_homem_mais_velho < idade:
                    idade_homem_mais_velho = idade
                    nome_homem_mais_velho = nome
        a = str(input('Agora virá as mulheres, correto? ')).capitalize()
        if a == 'Sim':
            for c in range(1, 3):
                nome = str(input('Qual o nome? '))
                idade = int(input('Qual idade? '))
                media_idade_soma += idade
                media_idade = media_idade_soma // 4
                if idade < 20:
                    quantidade_menor_de_20 += 1
        print(f'A média de idade do grupo é {media_idade}'.replace('[]', ''))
        print(f'O nome do homem mais velho do grupo é {nome_homem_mais_velho}')
        print(f'A quantidade de mulheres com menos de 20 anos é {quantidade_menor_de_20}')
    if capitalizado2 == str('Sim'):
        for c in range(1, 5):
            nome = str(input('Qual o nome? '))
            idade = int(input('Qual a idade? '))
            media_idade_soma += idade
            media_idade = media_idade_soma // 4
            if idade < int(20):
                quantidade_menor_de_20 += 1
    print(f'Tem {quantidade_menor_de_20} mulheres abaixo de 20 anos.')
    print(f'A média de idade do grupo [e {media_idade}]')
if capitalizado1 == str('Sim'):
    for c in range(1, 5):
        nome = str(input('Qual o nome? '))
        idade = int(input('Qual a idade? '))
        media_idade_soma += idade
        media_idade = media_idade_soma // 4
        if c == 1 or idade_homem_mais_velho < idade:
            nome_homem_mais_velho = nome
            idade_homem_mais_velho = idade
    print(f'A idade Média desse grupo é: {media_idade}')
    print(f'O homem mais valho desse grupo é {nome_homem_mais_velho}')
