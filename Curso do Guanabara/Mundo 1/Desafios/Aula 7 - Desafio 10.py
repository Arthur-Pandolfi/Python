print('Seja bem-vindo a calculadora de 5% de desconto do Tutu!')
produto = float(input('Digite aqui o valor do seu produto. RS'))
desconto = (produto * 5) / 100
total = produto - desconto
print('O preço do produto vai ser {:.2f}!'.format(total))
