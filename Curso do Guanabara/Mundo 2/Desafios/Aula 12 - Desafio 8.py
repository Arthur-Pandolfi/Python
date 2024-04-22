peso = float(input('Qual seu peso em KG? '))
altura = float(input('Qual a sua altura em Metros? '))
imc = peso / (altura ** 2)
print(f'O IMC dessa pessoa é \033[35m{imc:.2f}\033[m!')
if imc < float(18.5):
    print(f'Você está abaixo do peso por ter um IMC abaixo de 18.5.')
elif imc > float('18.5') and imc < float('25'):
    print(f'Você está no peso ideal, por ter um IMC entre 18,6 e 24.')
elif imc > float('25') and imc < float('30'):
    print(f'Você está com sobrepeso, por ter um IMC entre 25 e 30.')
elif imc > float('30') and imc < float('40'):
    print(f'Você está com obesidade, por ter um IMC entre 26 e 40')
elif imc > float('40'):
    print(f'Você está com obesidade mórbida, por ter um IMC maior que 40.')
