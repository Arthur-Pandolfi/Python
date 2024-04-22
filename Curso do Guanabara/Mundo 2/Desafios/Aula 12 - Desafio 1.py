from time import sleep
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o seu salário. R$: '))
anos = int(input('Digite em quantos anos você deseja pagar: '))
prestacao = valor / (anos * 12)
minimo = prestacao < (salario * 0.30)
print(f'Você quer  pagar um empréstimo de {anos} anos, tendo um salário de R${salario}, correto? ')
a = str(input('Sim/Não '))
capitalizado = a.capitalize()
if capitalizado == 'Sim':
    print('Ok, processando...')
    sleep(3)
    if minimo == True:
        print('Seu empréstime foi aprovado!')
    else:
        print('Empréstimo negado.')
