cara = float(input('Digite o quanto você vai andar nessa viagem em KMs: '))
if cara >= 200:
    a = cara * 0.45
    print(f'Você pagara R${a} nessa viagem, por andar {cara}KMs')
else:
    b = cara * 0.50
    print(f'Você pagara R${b} nessa viagem, por andar {cara}Kms')
