# Bibliotecas
from time import sleep

# Variaveis
idade = 0
sexo = ''
continuar = ''
maior18 = 0
homens = 0
mulher20 = 0

# Loop
print('CADASTRADOR DE PESSOAS')
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: ')).capitalize()
    # Verifica se o valor é valido
    while sexo != 'M' and sexo != 'F':
        print('VALOR INVÁLIDO, TENTE NOVAMENTE')
        sexo = str(input('Sexo: ')).capitalize()
    continuar = str(input('Quer continuar? [S/N] ')).capitalize()
    # Começa a verificação de idade, sexo e muulheres abaixo de 20
    if idade >= 18:
        maior18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade <= 20:
        mulher20 += 1
    # Verifica se o valor é valido
    while continuar != 'S' and continuar != 'N':
        print('VALOR INVÁLIDO, TENTE NOVAMENTE')
        continuar = str(input('Quer continuar? [S/N] ')).capitalize()
    if continuar == 'N':
        print('Ok, encerrando programa em:')
        for c in range(3, 0, -1):
            print(c)
            sleep(1)
            sleep(1)
        break

print(f'Foi cadastradas {maior18} pessoas com mais de 18 anos, {homens} homens e {mulher20} mulheres com menos de 20 anos')
sleep(2)
print('PROGRAMA ENCERRADO')