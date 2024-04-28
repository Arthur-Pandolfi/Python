# Tuplas & Variáveis
products = (
            'Lápis', 1.75,
            'Livro', 2.00,
            'Caderno', 15.90,
            'Estojo', 25.00,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canteas', 22.30,
            'Livro', 34.90
           )
position = 0

# Código
#Exbie ao usuário do que o código se trata
print("-" * 35)
print("         LISTAGEM DE PREÇO")
print("-" * 35)

# Começo da tabela
for position in range(0, len(products)):
    if (position % 2) == 0:
        print(f'{products[position]:.<30}', end='')
    else:
        print(f'R${products[position]:>7.2f}')
        
