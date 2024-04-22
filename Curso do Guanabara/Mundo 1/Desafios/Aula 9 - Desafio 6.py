print('Seja bem-vindo ao descobridor do seu primeiro e ultimo nome do Tutu!')
nome = str(input('Digite seu nome completo, para saber seu primeiro e ultimo nome! '))
base = nome.split()
nome1 = base[0]
nome2 = base[2]
print(f'No nome {nome}, o primeiro nome é {nome1} e o ultimo nome é {nome2}!')
