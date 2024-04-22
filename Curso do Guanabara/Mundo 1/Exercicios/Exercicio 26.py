algo = str(input('Digite uma frase: '))
maius = algo.count('A')
minus = algo.count('a')
div = algo.strip()
inicio = algo.find('A')+1
fim = algo.rfind('a')+1
print(f'Na frasa {algo}, a letra "A" aparece maiuscula {maius} vezes, {minus} vezes.\nA primeira letra "A"'
      f' aparece na posição {inicio} e a ultima na posição {fim}.')
