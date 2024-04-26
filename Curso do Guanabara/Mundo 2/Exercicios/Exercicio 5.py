nota1 = float(input('Digite a nota do primeiro semestre: '))
nota2 = float(input('Digite a nota do segundo semestre: '))
media = (nota1 + nota2) / 2
if media == 5 or media < 4.9:
    print(f'REPROVADO')
elif media == 5 or media < 6.9:
    print(f'RECUPERAÇÃO')
elif media > 7:
    print(f'APROVADO')
