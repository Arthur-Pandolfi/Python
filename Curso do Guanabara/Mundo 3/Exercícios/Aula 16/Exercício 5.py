# Variáveis & Tuplas
products = (
    'Lápis', 2.30,
    'Borracha', 2.00,
    'Caderno', 15.90,
    'Estojo', 25.00,
    'Transferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90
           )
position = 0

# Código
for position in range(0, len(products)):
    if (position % 2) == 0:
        print(f'{products[position]:.<30}', end='')
    if (position % 2) == 1:
        print(f'R$ {products[position]:>7.2f}')