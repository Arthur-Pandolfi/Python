print('Seja bem-vindo ao descobridor de unidade, dezena, centena e milhar do Tutu!')
base = str(input('Digite um número para saber sua unidade, dezena, centena e milhar! Obs(só funciona'
                 'números de 1 a 9999) '))
milhar = base[0]
centena = base[1]
dezena = base[2]
unidade = base[3]
print(f'A unidade do número {base} é {unidade}, a dezena é {dezena}, a centena é {centena}'
      f' e o milhar é {milhar}!')
