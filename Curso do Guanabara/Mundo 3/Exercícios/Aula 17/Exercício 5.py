from time import sleep
# Listas
numbers = []
pair_numbers = []
odd_numbers = []
# Váriaveis
want_to_continue = int
number_to_add = int
list_to_show = int

# Código Principal
# Checa os números que serão adicionados, e pergunta se o usuário quer continuar ou não a digitar números
while want_to_continue != 2:
    number_to_add = float(input('Escreve o número desejado: '))
    numbers.append(number_to_add)
    want_to_continue = int(input('Deseja continuar a adicionar números?\n[1] -> Sim\n[2] -> Não\n'))
    while want_to_continue != 1 and want_to_continue != 2:
        print('VALOR INVÁLIDO, TENTE NOVAMENTE.')
        want_to_continue = int(input('Deseja continuar a adicionar números?\n[1] -> Sim\n[2] -> Não\n'))
print()
print('Ok, vamos começar as análises desses números adicionados!')
want_to_continue = int # Reseta o valor da variavel para ser usado depois
sleep(1)

# Verifica a lista inteira com um loop FOR, e divide os números digrados em PAR ou IMPAR
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        pair_numbers.append(numbers[i])
    else:
        odd_numbers.append(numbers[i])
print('Checagem finalizada!')
del(i)
sleep(1)
print()

# Pergunta ao usuário qual lista ele quer analisar, a com todos os NÚMEROS, a so com números PARES, ou só com números IMPARES
while want_to_continue != 2: # Apenas para teste, adicionar uma variavel de fim
        print('Qual lista você quer visualizar?\n[1] -> Todos os números\n[2] -> Números Pares\n[3] -> Números Impares')
        list_to_show = int(input(''))
        # Checa se foi digitado um valor válido
        while list_to_show != 1 and list_to_show != 2 and list_to_show != 3:
            sleep(0.5)
            print()
            print('VALOR INVÁLIDO, TENTE NOVAMENTE.')
            print()
            sleep(0.5)
            print('Qual lista você quer visualizar?\n[1] -> Todos os números\n[2] -> Números Pares\n[3] -> Números Impares')
            list_to_show = int(input(''))
        # Em cada checagem, se faz um loop FOR para percorrer todos os itens da lista e exibe-lo em forma de STRING normal, sem parecer que foi usado uma lista. Ex: ['1', '2']
        # Checa se foi digitado o número 1, e exibe a lista com todos os números
        if list_to_show == 1:
            print('Ok, vamos mostrar a lista com todos os números!\n')
            for i in range(len(numbers)):
                print(numbers[i], end=' ')
            print()
            print('Pronto, essa foi a lista dos números digitados!\n')
        # Checa se foi digitado o número 2, e exibe a lista com os números pares
        elif list_to_show == 2:
            print('Ok, vamos mostrar a lista com os números pares!\n')
            for i in range(len(pair_numbers)):
                print(pair_numbers[i], end=' ')
            print()
            print('Pronto, essa foi a lista dos números pares digitados!\n')
        # Checa se foi digitado o número 1, e exibe a lista com todos os números
        elif list_to_show == 3:
            print('Ok, vamos mostrar a lista com os números pares!\n')
            for i in range(len(odd_numbers)):
                print(odd_numbers[i], end=' ')
            print()
            print('Pronto, essa foi a lista dos números impares digitados!\n')
        # Encerra as checagens, e pergunta se o usuário quer continuar mostrando os números
        print('Você quer continuar a visualizar os números?\n[1] -> Sim\n[2] -> Não')
        want_to_continue = int(input(''))
        while want_to_continue != 1 and want_to_continue != 2:
            sleep(0.5)
            print()
            print('OPÇÃO INVÀLIDA, TENTE NOVAMENTE.')
            print()
            sleep(0.5)
            print('Você quer continuar a visualizar os números?\n[1] -> Sim\n[2] -> Não')
            want_to_continue = int(input(''))
        print()