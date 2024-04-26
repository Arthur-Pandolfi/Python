reta1 = float(input('Qual o valor da primeira reta? '))
reta2 = float(input('Qual o valor da segunda reta? '))
reta3 = float(input('Qual o valor da terceira reta? '))
a = (reta1 + reta2) > reta3 and (reta2 + reta3) > reta1 and (reta3 + reta1) > reta2
if a == False:
    print(f'Esse valores formam um Triângulo.')
    if reta1 == reta2 and reta2 == reta3 and reta1 == reta3:
        print(f'Esse Triângulo é Equilatero.')
    if reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print(f'Esse Triângulo é Isóceles.')
    if reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
        print(f'Esse Triângulo é Escaleno')
else:
    print(f'Esse valores não formam um Triângulo.')