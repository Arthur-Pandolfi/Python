salario = float(input('Digite seu salário: '))
if salario > 1250.00:
    aumento = (salario * 10) / 100 + salario
    print(f'Antes você recebia {salario:.2f}, agora com 10% de aumento, você vai receber {aumento:.2f}!')
else:
    aumento = (salario * 15) / 100 + salario
    print(f'Antes você recebia {salario:.2f}, agora com 15% de aumento, você vai receber {aumento:.2f}!')
