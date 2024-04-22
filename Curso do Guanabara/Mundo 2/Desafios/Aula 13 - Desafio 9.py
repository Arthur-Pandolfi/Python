print('=' * 49)
print('10 PRIMEIROS NÚMEROS DE UMA PROGRESSÂO ARITMÉTICA')
print('=' * 49)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Qual a razão? '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' ')
print('ACABOU')