from random import randint

# Variaveis
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
position = 0
largest_number = 0
largest_number_position = 0
smaleest_number_position = 0
smaleest_number = 100000000000000000000000000000000000

# Código
number1 = randint(0, 10000000000000000000000000000000)
number2 = randint(0, 10000000000000000000000000000000)
number3 = randint(0, 10000000000000000000000000000000)
number4 = randint(0, 10000000000000000000000000000000)
number5 = randint(0, 10000000000000000000000000000000)

# Tupla
numbers = (
    number1,
    number2,
    number3,
    number4,
    number5
        )

print("Lista de números: ")
for c in numbers:
    position += 1
    print(f"{position}º number: {c}")
del(c)
position = 0

for c in numbers:
    position += 1
    if c > largest_number:
        largest_number  = c
        largest_number_position = position
del(c)
position = 0

for c in numbers:
    position += 1
    if smaleest_number > c:
        smaleest_number = c
        smaleest_number_position = position

print(f"-" * 50,
      f"\nMenor número: {smaleest_number}\n"
      f"Posição do menor Número: {smaleest_number_position} \n"
      f"Maior Número: {largest_number} \n"
      f"Posição do Maior Número: {largest_number_position}")

# RESOLUÇÃO DO GUANABARA
max(numbers) # Maior valor da tupla
min(numbers) # Menor valor da tupla
