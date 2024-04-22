nome = str(input('Digite seu nome:')).strip()
maius = nome.upper()
minus = nome.lower()
total = len(nome)
espaco = len(nome.replace(' ', ''))
dividido = nome.split()
total1 = len(dividido[0])
print(f'O nome {nome} em maiusculo fica {maius}, minusculo fica {minus}, no total tem {total}'
      f'no total sem espaços tem {espaco} e o primeiro nome dele é {dividido[0]}, \ntendo {total1} de '
      f'letras.')
# Tambem é possivel saber o primeiro nome usando "variavel.find(' ')"
