from time import sleep

print(f'Estourando fogos em:')
for c in range(10, -1, -1): # O menos um é para ele contar até 0, por o ultimo número ser ignorado
    print(c)
    sleep(1)

print('Fogos Estourados!')