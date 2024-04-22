from math import cos, tan, sin, radians
angulo = float(input('Digite o ângulo desejado: '))
print(f'O valro de Cosseno é {cos(radians(angulo)):.2f}, de Tangente é {tan(radians(angulo)):.2f}, '
      f'e o valor de Seno é' f' {sin(radians(angulo)):.2f}')
