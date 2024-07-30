# Variaveis
numbers = []
number_to_add = float
want_to_continue = 1

# Código Princpal
print('Seja bem vindo ao meu programa que vai analisar ua lista, e imprir essa lista em ordem crscente, se tem o numero 5 e quantos números foram digitados!!')

while True:
    number_to_add = float(input('Digite o número desejado: '))
    want_to_continue = int(input('Quer continuar a digitar números?\n[1] -> Sim\n[2] -> Não\n'))
    numbers.append(number_to_add)
    while want_to_continue != 1 and want_to_continue != 2:
        print('VALOR DIGITADO INVALIDO. TENTE NOVAMENTE.')
        want_to_continue = int(input('Quer continuar a digitar números?\n[1] -> Sim\n[2] -> Não\n'))
    if want_to_continue == 2:
        break

print()
print('Agora, vamos analisar essa lista!')
print('O número 5 foi digitado?')
if 5 in numbers:
    print('O número 5 foi digitado.')
else:
    print('O número 5 não foi digitado.')
print('Quatos números foram digitados?')
print(f'Foram digitados {len(numbers)} números')
print('Como fica essa lista em ordem crscente?')
print('Fica assim!')
numbers.sort(reverse=True)
for x in range(0, len(numbers)):
    print(numbers[x], end=' ')