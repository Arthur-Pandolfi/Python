print('Seja bem-vindo a calculadora de quantidade de tinta que precisa para pintar uma parede!')
altura = int(input('Qual a altura da sua parede? '))
largura = int(input('Qual a largura da sua parede?'))
tamanho = largura * altura
tinta = tamanho / 2
print('De acordo com o tamanho da sua parede {}m², você vai precisar de {}L de tinta, considerando que cada litro pinta'
' 2m²'.format(tamanho, tinta))
