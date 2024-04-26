# Variaveis
nome_produto_atual = ""
nome_produto_mais_barato = ""
continuar_comprando = ""
quantidade_maior_de_1k = 0
preco_produto_mais_barato = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
preco_produto_atual = 0
quantidade_de_compras = 0
total_gasto = 0

# Exibe ao usuário do que o programa se trata
print("-=-"  * 10)
print("         Lojas tutu          ")
print("-=-" * 10)

# Início
while True:
    nome_produto_atual = str(input("Qual produto deseja adquirir agora? ")).strip().capitalize()
    preco_produto_atual = int(input("Qual o valor desse produto? R$"))
    continuar_comprando = str(input("Deseja continuar comprando itens? [S/N] ")).strip().capitalize()
    quantidade_de_compras += 1

    # Calcula o total gasto na compra
    total_gasto += preco_produto_atual

    # Verifica se o produto custa mais de 1000 reais
    if preco_produto_atual >= 1000:
        quantidade_maior_de_1k += 1

    # Verifica o nome do produto mais barato
    if preco_produto_mais_barato > preco_produto_atual:
        preco_produto_mais_barato = preco_produto_atual
        nome_produto_mais_barato = nome_produto_atual

    # Verifica se a pessoa quer continuar comprando
    if continuar_comprando == "N":
        break
print(f"Você comprou {quantidade_de_compras} itens, {quantidade_maior_de_1k} produtos que custam mais de 1000 reais, o nome do produto mais " 
      f"baratoadiquirido foi {nome_produto_mais_barato}, o preço dele é R${preco_produto_mais_barato}."
      f"\nO total gasto na compra foi: {total_gasto}")