# Variáveis
numbers = []
number_to_add = float
want_to_continue = 1

# Código Principal
print('Seja bem vindo ao meu programa que mostra os números digitados dentro de uma lista em ordem crescente!')
while True:
    if want_to_continue == 2:
        break
    number_to_add =float(input('Digite o valor desejado: '))
    if number_to_add not in numbers:
        numbers.append(number_to_add)
    want_to_continue = int(input('Você quer continuar digitando números?\n[1] --> Sim\n[2] --> Não\n'))
    while want_to_continue != 1 and want_to_continue != 2:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        want_to_continue = int(input('Você quer continuar digitando números?\n[1] --> Sim\n[2] --> Não\n'))

print('Lista dos números digitados em ordem crscente: ', end=' ')
numbers.sort()
for i in range(len(numbers)):
    print(numbers[i], end=' ')
