from random import randint
pc = randint(0,2)
cara = int(input("""Escolha UM:
 [0] = Papel
 [1] = Pedra
 [2] = Tesoura
  """))
if cara == pc:
    print('Empatamos!')
elif cara == int('0') and pc == int('1'):
    print('Você ganhou!')
elif cara == int('0') and pc == int('2'):
    print('Eu ganhei!')
elif cara == int('1') and pc == int('0'):
    print('Eu ganhei!')
elif cara == int('1') and pc == int('2'):
    print('Você ganhou!')
elif cara == int('2') and pc == int('1'):
    print('Eu ganhei!')
elif cara == int('2') and pc == int('0'):
    print('Você ganhou!')