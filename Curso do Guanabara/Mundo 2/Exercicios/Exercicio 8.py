peso = float(input('Qual seu peso em KG? '))
altura = float(input('Qual sua altura em Metros? '))
imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print(f'Abaixo do Peso.')
elif imc == 18.5 or imc < 25:
    print(f'Peso Ideal.')