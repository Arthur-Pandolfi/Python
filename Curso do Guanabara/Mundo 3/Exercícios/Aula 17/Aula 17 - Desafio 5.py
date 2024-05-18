# IMPORTAÇÔES
from time import sleep
# FIM DAS IMPORTAÇõES

# Variáveis & Listas
numbers = [] #Todos os números digitados cairam aqui
sorted_numbers = [] #Todos os números digitados em ordem Crescente, para melhor visualização
sorted_pair_numbers = [] #Todos os números digitados que forem pares em ordem Crescente
pair_numbers = [] #Todos os números digitados que forem impáres sem estar em ordem Crescente
sorted_odd_numbers = [] #Todos os números digitados que forem Impáres em ordem crescente
odd_numbers = [] #Todos os números digitados que forem ímpares sem estar em oredem Crescente
number_to_add = 0 #Número que o usuário deseja adicionar
position = 0 #Posição que o loop "for" está na quele momento
sorrted_or_no = 0 #Se o usuário que ver os números digitados em ordem Crescente ou não
want_to_continue = '' #Se o usuário que continuar a adicionar números no loop "while" infinito

# Código
while True:
    number_to_add = int(input('Digite um número para adicionar a lista: '))
    numbers.append(number_to_add)
    want_to_continue = str(input('Quer continuar? [S/N]\n')).strip().capitalize()
    while want_to_continue != 'S' and want_to_continue != 'N':  #Checa se o usuário escreveu um valor valido
        print('OPÇÃO INVÀLIDA, TENTE NOVAMENTE')
        sleep(0.2)
        want_to_continue = str(input('Quer continuar? [S/N] ')).strip().capitalize()
    if want_to_continue == 'N':  #Checa se o usuário que parar
        break
    sleep(0.2)

sorted_numbers = sorted(numbers) #Organiza os números em ordem crescente

# CHECAGEM DOS N{ÚMEROS PARES E IMPÁRES}
for position in range(len(sorted_numbers)): #Distribui os números pares e impáres em listas diferentes
    if (sorted_numbers[position] % 2) == 0: #Checa se o número atual é par
        sorted_pair_numbers.append(sorted_numbers[position]) #Adiciona o número atual a lista de números pares em ordem Crescnte
        pair_numbers.append(numbers[position]) #Adiciona o número atual a lista de números pares sem estar na ordem Crescnte
    elif (sorted_numbers[position] % 2) != 0: #Checa se o número atual é impar
        sorted_odd_numbers.append(sorted_numbers[position]) #Adiciona o número atual a lista de números impáres em ordem Crescnte
        odd_numbers.append(numbers[position]) #Adiciona o número atual a lista de números impáres sem estar na ordem Crescnte
position = 0 #Altera o valor da variável para 0, par ser usada nos loops "For" abaixo

print('-=-' * 10)

#EXIBIE OS NÚMEROS DIGITADOS SEM ESTAR SEPARADO OS PARES E IMPÁRES
#LINHA A BAIXO: Pergunta so usuário se ele quer ver os números na ordem crescente, na ordem Digitada, ou em ordem Decrescente
sleep(0.5)
sorrted_or_no = int(input('Você deseja ver os números em ordem Crescente[1], na ordem que foi Digitada[2], ou na ordem Decrescente[3]? ')) 
while sorrted_or_no != 1 and sorrted_or_no != 2 and sorrted_or_no != 3: #Checa se o usuário entrou com uma resposta inválida
    sleep(0.2)
    print('OPÇÃO INVÀLIDA, TENTE NOVAMENTE')
    sleep(0.2)
    sorrted_or_no = int(input('Você deseja ver os números em ordem Crescente[1], na ordem que foi Digitado[2] ou na ordem decrescente[3]? '))
if sorrted_or_no == 1: #Checa se o usuário quer os números em ordem Crescente
    print('Ok, aqui está os números digitados em ordem Crescente:')
    for position in range(len(sorted_numbers)): #Exibe os todos os números digitados, indenpendete se é par ou ímpar
        print(sorted_numbers[position], end=' ')
    sleep(0.5)
elif sorrted_or_no == 2: #Checa se o usuário quer os números na ordem Digitada
    print('Ok, aqui está os números digitados na ordem Digitada: ')
    for position in range(len(numbers)):
        print(numbers[position], end=' ')
    sleep(0.5)
elif sorrted_or_no == 3: #Checa se o usuário quer os números em ordem Decrescente
    print('Ok, aqui está os números digitados em ordem Decrescente:')
    for position in range(len(sorted_numbers) -1, -1, -1):
        print(sorted_numbers[position], end=' ')
    sleep(0.5)
print()
sorted_or_no = '' #Altera o valor da variável para 0, para ser usado novamente na hora de exibir os números pares e impáres
position =  0 #Altera o valor da variável paro 0, para ser usado novamente nos loops "For" abaixo, para exibir o número da lista, sem aparecer no formato padrão
print('-=-' * 10)

#EXIBIE OS NÚMEROS PARES
if len(pair_numbers) == 0: #Checa se foi digitado números pares
    print('Não foi digitado números Pares')
    print('-=-' * 10)
else:
    #LINHA ABAIXO: Pergunta ao usuário se ele quer ver os números pares na ordem crescente, que foi digitada, ou decrescente 
    sorrted_or_no = int(input('Você quer ver os números PARES em ordem Crescente[1], na ordem que foi Digitada[2], ou na ordem Decrescente[3]? '))
    while sorrted_or_no != 1 and sorrted_or_no != 2 and sorrted_or_no != 3: #Checa se o usuário entrou com uma opção inválida
        sleep(0.2)
        print('OPÇÃO INVÀLIDA, TENTE NOVAMENTE')
        sleep(0.2)
        sorrted_or_no = int(input('Você quer ver os números PARES em ordem Crescente[1], na ordem que foi Digitada[2], ou na ordem Decrescente[3]? '))

    if sorrted_or_no == 1: #Checa se o usuário quer ver os números pares em ordem Crescente
        print('Ok, aqui está os números pares digitados em ordem Crescente:')
        for position in range(len(sorted_pair_numbers)):
            print(sorted_pair_numbers[position], end=' ')
        sleep(0.5)
    elif sorrted_or_no == 2: #Checa se o usuário quer vre os números pares na ordem Digitada
        print('OK, aqui está os números pares digitados na ordem Digitada:')
        for position in range(len(pair_numbers)):
            print(pair_numbers[position], end=' ')
        sleep(0.5)
    elif sorrted_or_no == 3: #Cehca se o usuário quer ver os números pares em ordem Decrescente
        print('OK, aqui está os números pares digitados na ordem Decrescente:')
        for position in range(len(sorted_pair_numbers) -1, -1, -1):
            print(sorted_pair_numbers[position], end=' ')
        sleep(0.5)
print()
print('-=-' * 10)
sorrted_or_no = '' #Altera o valor da variável para 0, para ser usado novamente na hora de exibir os números pares e impáres
position =  0 #Altera o valor da variável paro 0, para ser usado novamente nos loops "For" abaixo, para exibir o número da lista, sem aparecer no formato padrão

#EXIBIE OS NÚMEROS IMPÁRES
if len(odd_numbers) == 0: #Cehca se tem números impáres digitados
    print('Não foi digitado números Impáres')
    print('-=-' * 10)
else:
    sorrted_or_no = int(input('Você deseja ver os números Impáres em ordem Crescente[1], na ordem que foi Digitada[2], ou na ordem Decrescente[3]? '))
    #LINHA ABAIXO: Pergunta ao usuário se ele quer ver os números Impáres na ordem crescente, que foi digitada, ou decrescente 
    while sorrted_or_no != 1 and sorrted_or_no != 2 and sorrted_or_no != 3:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
        sorrted_or_no = int(input('Você deseja ver os números em ordem Crescente[1], na ordem que foi Digitada[2], ou na ordem Decrescente[3]? '))

    if sorrted_or_no == 1: #Checa se o usuário quer ver os números impáres digitados na ordem Crescente
        print('Ok, aqui está os números impáres na ordem Crescente:')
        for position in range(len(sorted_odd_numbers)):
            print(odd_numbers[position], end=' ')
        sleep(0.5)
    elif sorrted_or_no == 2: #Checa se o usuário quer ver os números impáres na ordem que foi Digitada
        print('OK, aqui está os números impáres na ordem Digitada:')
        for position in range(len(odd_numbers)):
            print(odd_numbers[position], end=' ')
        sleep(0.5)
    elif sorrted_or_no == 3: #Cehca se o usuário quer ver os números impáres na ordem decrescente
        print('Ok, aqui estpa os números impáres na ordem Decrescente:')
        for position in range(len(sorted_odd_numbers) -1, -1, -1):
            print(sorted_odd_numbers[position], end=' ')
        sleep(0.5)
print('-=-' * 10)
