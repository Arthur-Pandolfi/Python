vel = float(input('Digite a velocidade do carro: '))
perm = 80
if vel > perm:
    acima = vel - perm
    multa = acima * 7
    print(f'Você receberá R${multa} de multa, por extrapolar o limite permitido.')
else:
    print('Você está na velocidade permitida')