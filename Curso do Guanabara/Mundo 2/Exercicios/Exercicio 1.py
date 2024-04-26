from time import sleep
casa = float(input('Qual o valor da casa? '))
salario = float(input('Digite o valor do seu salário: '))
tempo = int(input('Você quer pagar ela em quantos anos? '))
prestacao = casa / (tempo * 12)
aprovado_ou_nao = prestacao < (salario * 30) / 100
print(f"""Você quer fazer um empréstimo de {tempo} anos, de uma casa de R${casa} e tendo um salário de R$ {salario}
.Correto?""")
sim = str(input('Sim/Não '))
capitalizado = sim.capitalize()
if capitalizado == 'Sim':
    print('Ok')
    sleep(1)
    print('Processando...')
    sleep(3)
    if aprovado_ou_nao == True:
        print('\033[1;32mEMPRÈSTIMO APROVADO\033[m')
    else:
        print('\033[1;31mEMPRÉSTIMO NEGADO\033[m')
if capitalizado == 'Não':
    print('Ok, Encerrando o programa em\n3')
    sleep(1)
    print('2')
    sleep(1)
    print('Programa encerrado.')
