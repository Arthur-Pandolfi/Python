salario = float(input('Digite seu salario: '))
aumetno = salario
if salario < 1250.00:
    aumetno = ((salario * 15) / 100) + salario
else:
    aumetno = ((salario * 10) / 100) + salario
print(f'Você recebia {salario}, e agora vai receber {aumetno}!')
