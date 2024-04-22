kms = float(input('Você rodou quantos KM com esse carro? '))
dias = int(input('Você ficou quantos dias com esse carro? '))
print(f'Você vai ter que pagar R${(dias * 60) + (kms * 0.15)} por ter ficado com ele por {dias}'
      f' e ter rodado {kms} de KMs com ele!')
