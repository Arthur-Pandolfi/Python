print('Seja bem-vindo ao descobridor de quantos A tem em uma palavra!')
base = str(input('Digite uma palavra para descobrir quantos "As" tem nessa palavra!'))
stripado = base.strip()
a = stripado.count('A')
b = stripado.count('a')
a1 = stripado.find('A')
a2 = stripado.find('a')
print(f'A palavra "{stripado}" tem {a} "As" maiusculos e {b} "As" minúsculos.\n'
      f'O primeiro "A" da palavra "{base}" aparece na posição {a1} e a ultima na posição '
      f'{a2} ')
