cara = float(input('Digite a distância da viagem: '))
if cara <= 200:
    menor = cara * 0.50
    print(f'Você vai pagar R${menor:.2f} nessa viagem de {cara:.2f}KMs!')
else:
    maior = cara * 0.45
    print(f'Você vai pagar {maior:.2f} nessa viagem de {cara:.2f}KMs')
