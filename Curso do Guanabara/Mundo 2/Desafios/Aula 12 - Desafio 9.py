from time import sleep
preco = float(input('\033[1;32mDigite o valor do produto\033[m: \033[1;35mR$\033[m'))
pagamento = str(input('\033[1;31mDigite a forma de pagamento\033[m: \033[1;36mDinheiro/Cheque/Cartão\033[m '))
capitalizado = pagamento.capitalize()
if capitalizado == 'Dinheiro':
    print('Ok')
    sleep(1)
    print('Processando...')
    sleep(3)
    dinheiro = (preco * 10) / 100
    dinheiro1 = preco - dinheiro
    print(f'O preço a ser pago com 10% de desconto vai ser R${dinheiro1}!')
if capitalizado == 'Cheque':
    print('Ok')
    sleep(1)
    print('Processando...')
    sleep(3)
    cheque = (preco * 10) / 100
    cheque1 = preco - cheque
    print(f'O preço a ser pago com 10% de desconto vai ser R${cheque1}!')
if capitalizado == 'Cartão':
    sim = str(input(f'Vai ser parcelado? \033[1;32mSim/Não\033[m '))
    capitalizado1 = sim.capitalize()
    if capitalizado1 == 'Sim':
        print(f'Ok')
        parcela = int(input('Vai ser em quantas vezes? 1 a 12: '))
        if parcela == int('1'):
            print('Ok')
            sleep(1)
            print('Processando...')
            sleep(3)
            parcela1 = (5 * preco) / 100
            parcela12 = preco - parcela1
            print(f'O preço a ser pago com 5% de desconto vai ser R${parcela12}')
        if parcela == int('2'):
            print('Ok')
            sleep(1)
            print('Processando...')
            sleep(3)
            print(f'O valor a ser pago vai ser R${preco}!')
        if parcela == int('3') or parcela > int('3'):
            print('Ok')
            sleep(1)
            print('Processando...')
            sleep(3)
            parcela3 = (20 * preco) / 100
            parcela3_1 = preco + parcela3
            print(f'O valor a ser pago vai ser {parcela3_1}!')
