numero = 0


while True:
    print('Digite um núemro para ver sua tabuada! (números negativo para encerrar)')
    numero = int(input('Digite um número: '))
    if 0 > numero:
        print('PROGRAMA ENCERRADO')
        break
    else:
        for c in range(1, 11):
            print(f'{numero} x {c} = {numero * c}')