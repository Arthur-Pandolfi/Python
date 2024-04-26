# Variáveis
valor_para_ser_sacado = 0
valor_loop = 0
cedulas_50 = 0
cedulas_20 = 0
cedulas_10 = 0
moedas_1 = 0

# Informa ao usuário do que o programa se trata
print("-=-" * 12)
print(" Caixa Eletrônico - Banco do Brasil ")
print("-=-" * 12)

# Pergunta qual o valor desejado para ser sacado
valor_para_ser_sacado = int(input("Qual valor o senhor(a) deseja sacar? "))

# Início
while True:
    if (valor_para_ser_sacado - valor_loop) % 50 == 0:
        cedulas_50 += 1
        valor_loop += 50

    elif (valor_para_ser_sacado - valor_loop) % 20 == 0:
        cedulas_20 += 1
        valor_loop += 20

    elif (valor_para_ser_sacado - valor_loop) % 10 == 0:
        cedulas_10 += 1
        valor_loop += 10

    elif (valor_para_ser_sacado - valor_loop) % 1 == 0:
        moedas_1 += 1
        valor_loop += 1
    
    if valor_loop == valor_para_ser_sacado:
        break

# Exibie para o usuário quntas cédulas e moedas foi necessárias sacar
print("-" * 50)
print(f"Cédulas de 50 --> {cedulas_50}")
print(f"Cédulas de 20 --> {cedulas_20}")
print(f"Cédulas de 10 --> {cedulas_10}")
print(f"Moedas de 1 --> {moedas_1}")
print("-" * 50)