from random import shuffle
item1 = str(input('Primeira pessoa: '))
item2 = str(input('Segunda pessoa: '))
item3 = str(input('Terceira pessoa: '))
item4 = str(input('Quarta pessoa: '))
lista = [item1, item2, item3, item4]
shuffle(lista)
print('A ordem vai ser:', lista)
