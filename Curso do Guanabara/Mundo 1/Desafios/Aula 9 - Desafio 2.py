print('Seja bem-vindo ao algum treco de nome do Tutu!')
nome = str(input('Qual seu nome? '))
maius = nome.upper()
minus = nome.lower()
sem = len(nome.replace(' ', ''))
nomea = nome.split()[0]
print(f'No nome {nome}, ele escrito em maiúsculo seria {maius}, ele em minusculo seria'
      f' {minus}, ele sem espaços tem {sem} letras e a primeira palavra dele é {nomea}')
