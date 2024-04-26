# Variaveis
sexo = ''

# Pergunta o sexo do usuario
sexo = str(input('Digite seu sexo [M/F]: ')).capitalize()

# Loop

while sexo != 'M' and sexo != 'F':
    print('\033[31mDados Inválidos.\033[m\nDigite um valor valido.')
    sexo = str(input('Digite seu sexo novamente: ')).capitalize()