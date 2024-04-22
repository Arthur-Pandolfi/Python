print('Digite seu sexo: [M/F]')

# Variaveis
sexo = str(input(''))
capitalizado = sexo.capitalize()

# Estrutura de Repetição
    # Cheque sexo != M/F
while capitalizado != 'M' and capitalizado != 'F':
    print('Resposta invalida')
    print('Digite seu sexo: [M/F]')
    sexo = str(input(''))
    capitalizado = sexo.capitalize  