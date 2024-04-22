maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Digite seu peso: '))
    if c == 1:
        maior = peso
        menor = peso
    if maior > peso:
        maior = peso
    if menor < peso:
        menor = peso
print(maior, menor)
# só pra n dar 13 ezzzz
