velocidade = float(input('Digite a quanto KM/H que você esta dirigindo: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você está dirigindo muito rápido! VocÊ vai ter que pagar R${multa} de multa!')
else:
    print('Parábens, você esta dirigindo na velocidade permitida!')
