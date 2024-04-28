# Variaveis & Tuplas
numero_escolhido = 0
numeros = (
            'um', 
           'dois', 
           'três', 
           'quatro', 
           'cinco', 
           'seis', 
           'sete', 
           'oito', 
           'nove', 
           'dez', 
           'onze', 
           'doze', 
           'treze', 
           'quartoze', 
           'quinze',
           'dezesseis', 
           'dezessete', 
           'dezoito', 
           'dezenove', 
           'vinte'
        )
print(len(numeros))
# Começo
numero_escolhido = int(input("Digite um númzero de 0 a 20: "))

while numero_escolhido > 20 or numero_escolhido < 0:
    print("Opção inválida. Tente Novamente.")
    numero_escolhido = int(input("Digite um número de 0 a 20: "))

if numero_escolhido == 0:
    print(f'Você digitou o número: zero')

else:
    print(f'Você digitou o número: {numeros[numero_escolhido - 1]}')
