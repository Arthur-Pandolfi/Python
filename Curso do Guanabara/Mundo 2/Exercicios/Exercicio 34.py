pessoas_cadastradas = 0
continuar = 'Y'
maior_de_18 = 0
homens_cadastrados = 0
mulher_maior_20 = 0

print('-' * 22)
print('CADASTRADOR DE PESSOAS')
print('-' * 22)

while True:
    sexo = str(input('DIGITE O SEXO [M/F]: ')).strip().capitalize()
    idade = int(input('DIGITE A IDADE: '))
    print('-' * 50)
    # Adiciona 1 a quantidade de pessoas cadastradas 
    pessoas_cadastradas += 1

    # Checa se foi cadastradar mais de um pesoa para continuar cadastrando
    if pessoas_cadastradas > 1:
        continuar = str(input('QUER CONTINUAR A CADASTRAR PESSOAS? [Y/N] ')).strip().capitalize()

    # Checa se a pessoa que continuar ou não
    if continuar == 'N':
        break

    # Checa quantas pessoas tem mais de 18 anos
    if idade >= 18:
        maior_de_18 += 1
    
    # Checa quantos homens foram cadastrados
    if sexo == 'M':
        homens_cadastrados += 1
    
    # Checa quantas mulheres com mais de 20 anos foram cadastradas
    if sexo == 'F' and idade >= 20:
        mulher_maior_20 += 1

print(f'Foram cadastradas {pessoas_cadastradas} pessoas, sendo {homens_cadastrados} homens, {mulher_maior_20} mulhe'
f'res com 20 anos ou mais, e {maior_de_18} pessoas com 18 anos ou mais.')

print('PROGRAMA ENCERRADO')
