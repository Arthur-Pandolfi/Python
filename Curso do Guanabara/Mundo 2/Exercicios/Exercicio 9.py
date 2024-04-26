from time import sleep
print(f'='*20, f'Lojas Tutu', f'='*20)
valor = float(input('Qual o valor do produto? R$'))
print(f'Forma De Pagamento')
print('''[ 1 ] Dinheiro 
[ 2 ] Cheque
[ 3 ] Cartão''')
pagamento = int(input('  '))
if pagamento == 1 or pagamento == 2:
    desconto_cheque_porcentagem = (valor * 10) / 100
    desconto_cheque = valor - desconto_cheque_porcentagem
    print(f'Ok')
    sleep(1)
    print('Processando...')
    sleep(3)
    print(f'O valor a ser pago com 10% de desconto vai ser R${desconto_cheque:.2f}!')
if pagamento == 3:
    print('Ok')
    sleep(1)
    print('Vai ser parcelado? ')
    parcelado = str(input('Sim/Não '))
    capitalizado1 = parcelado.capitalize()
    if capitalizado1 == 'Não':
        print('Ok')
        sleep(1)
        cartao_desconto_porcentagem = (valor * 5) / 100
        cartao_desconto = valor - cartao_desconto_porcentagem
        print(f'Processando')
        sleep(3)
        print(f'O valor a ser pago vai R${cartao_desconto:.2f} com 5% de desconto!')
    if capitalizado1 == 'Sim':
        parcelamento_vezes = int(input('Vai ser em quantas vezes? 2/3/4+\n'))
        if parcelamento_vezes == 2:
            parcelamento_2vezes = valor / 2
            print(f'O valor a ser pago vai ser R${parcelamento_2vezes}!')
        if parcelamento_vezes == 3 or parcelamento_vezes > 3:
            print(f'Ok')
            sleep(1)
            print(f'Processando...')
            sleep(3)
            parcelamento_3vezes_parte1 = valor * float(0.20)
            parcelamento_3vezes_parte2 = parcelamento_3vezes_parte1 / 10
            parcelamento_3vezes_parte3 = parcelamento_3vezes_parte2 * parcelamento_vezes
            print(f'O valor a ser pago vai ser R${parcelamento_3vezes_parte3:.2f}, com 20% de juros, pagando'
                  f' em {parcelamento_vezes} vezes.')
if pagamento < 1 or pagamento > 3:
    print(f'Opção INVALIDADA de pagamento, tente novamente')
print(f'='*20, f'Lojas Tutu', f'='*20)
