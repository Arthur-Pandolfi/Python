altura = float(input('Digite a altura de sua parede em Metros: '))
largura = float(input('Digite a largura de sua parede em Metros: '))
tamanho = largura * altura
tinta = tamanho / 2
print(f'Analisando a altura ({altura}) e largura ({largura}) de sua parede, você vai precisar de '
      f'{tinta} litros de tinta para pintar {tamanho}M²')
