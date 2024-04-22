valor = float(input('Digite o valor de um produto: R$'))
desconto = float(input('Digite o valor do desconto: '))
descontado = (desconto * valor) / 100
desconto_total = valor - descontado
print(f'De acordo com o valor em reais (R${valor}) e o desconto apresentado ({desconto}), o valor do '
      f'produto será R${desconto_total:.2f}!')
