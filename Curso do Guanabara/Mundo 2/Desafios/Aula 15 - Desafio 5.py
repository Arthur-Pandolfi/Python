# Variaveis
total_gasto = 0
maior_de_1000 = 0
preco_do_produto = 0
continuar_comprando = ''
preco_produto_mais_barato = 999999999999999999999999999999999999999999999999999999999999999999999999999999999
nome_produto_mais_barato = ''
produto_atual = ''

# Exibie para o usúario do que o programa se trata
print('-' * 30)
print('       Lojas do Tutu       ')
print('-' * 30)

# Início do Loop
while True:
    produto_atual = str(input('Qual produto você deseja pagar? ')).strip().capitalize()
    preco_do_produto = int(input('Qual o valor do produto? '))
    continuar_comprando = str(input('Deseja continuar comprando itens? [Y/N]')).strip().capitalize()

    # Checa se o produto atual é o mais barato
    if preco_produto_mais_barato >= preco_do_produto:
        nome_produto_mais_barato = produto_atual
        preco_produto_mais_barato = preco_do_produto
    
    # Checa se o produto é maior que MIL reais
    if preco_do_produto >= 1000:
        maior_de_1000 += 1
    
    # Calcula o total gasto na compra
    total_gasto += preco_do_produto

    # Checa se a pessoa que continuar ou parar de comprar
    if continuar_comprando == 'N':
        break

print(f'Foi gasto R${total_gasto} na compra, {maior_de_1000} produtos custam mais de 1000 reais, e o produto mais'
      f' barato foi o {nome_produto_mais_barato}')

