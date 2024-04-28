# Tupla & Varáveis
numbers = ('um',
           'dois',
           'tres',
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
user_input = 0

# Início
user_input = int(input('Digite um número: '))

if user_input == 0:
    print('O número 0 em extenso é igual a: zero')
elif user_input == 20:
    print('O número 20 por extenso é igual a: vinte')
else:
    print(f'O número {user_input} em extens é igual a: {numbers[user_input - 1]}')