# Variaveis & Tupla
numbers = (
            int(input("Digite o 1º Número: ")),
            int(input("Digite o 2º Número: ")),
            int(input("Digite o 3º Número: ")),
            int(input("Digite o 4º Número: ")),
          )
position = 0
nine_qunatity = 0
first_number3_position = 0
pair_numbers = 0

# Código

# Checa a quantidade de noves digitados
for x in numbers:
    if x == 9:
        nine_qunatity += 1

# Checa o primeiro número 3 dentro da tupla
for y in numbers:
    position += 1
    if y == 3:
        first_number3_position = position
        break


for z in numbers:
    if (z % 2) == 0:
        pair_numbers += 1

# Exibe ao usuário o resultado das verificações anteriores
print(f"Você digitou os números:", end=' ')

for c in numbers:
    print(c, end=' ')

print(f"\nO valor 9 apareceu {nine_qunatity} vezes")
if first_number3_position == 1 or first_number3_position == 2 or first_number3_position == 3 or first_number3_position == 4: 
    print(f"O primeiro valor 3 apareceu na posição: {first_number3_position}")
print(f"Os valores pares digitados foram:", end=' ')
for a in numbers:
    if (a % 2) == 0:
        print(a, end=' ')