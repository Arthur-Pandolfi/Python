nota1 = float(input('Qual a sua nota do primeiro bimestre? '))
nota2 = float(input('Qual a sua nota do segundo bimestre? '))
nota3 = float(input('Qual a sua nota do terceiro bimestre? '))
nota4 = float(input('Qual a sua nota do quarto bimestre? '))
unificado = nota1 + nota2 + nota3 + nota4
media = unificado / 2
if media < float('5.00'):
    print(f'REPROVADO!')
elif media == float('5.00') and float('6.90'):
    print(f'RECUPERAÇÃO')
else:
    print(f'APROVADO!')