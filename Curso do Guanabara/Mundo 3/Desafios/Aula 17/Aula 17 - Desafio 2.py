# Listas & Variáveis
numbers = []
numbers_sorted = []
number_to_add = 0
continuee = ''
position = 0

# Código

#Pergunta ao usuário o número que edseja adicionar
while True:
    number_to_add = int(input('Digite um número: '))
    while number_to_add in numbers:
        number_to_add = int(input('Opção Inválida, tento novamente.\nDigite um número: '))
    numbers.append(number_to_add)
    continuee = str(input('Deseja continuar? [s/n] ')).strip().capitalize()
    if continuee == 'N':
        break

# Exibie para o usuário os números digitados sem parecer em forma de lista
print(f'Você digitou os números: ',end='')
for position in range(0, len(numbers)):
    print(numbers[position], end=' ')
position = 0
print() # <-- Cria uma nova linha

# Agora exibe os números digitados em ordem crescente
numbers_sorted = numbers.sort()
print(f'Agora eles em ordem crescente: ', end='')
for position in range(0, len(numbers)):
    print(numbers[position], end=' ')
position = 0