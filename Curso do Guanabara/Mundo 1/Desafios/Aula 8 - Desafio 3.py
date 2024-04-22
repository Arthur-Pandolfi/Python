import math
angulo = float(input('Digite o valor do angûlo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor de SENO é {:.2f} \n O valor de COSSENO é {:.2f}\n O valor do TANGENTE é {:.2f}'.format(seno, cosseno, tangente))
