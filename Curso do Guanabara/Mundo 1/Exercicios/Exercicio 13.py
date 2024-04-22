salario = float(input('Digite seu salário: R$'))
aumento = float(input('Digite o aumento: '))
semi_descontado = (salario * aumento) / 100
print(f'De acordo com o salário informado (R${salario}), e o auemnto que ele recebera ({aumento}), '
      f'o novo salário sera de R${semi_descontado + salario:.2f}')
