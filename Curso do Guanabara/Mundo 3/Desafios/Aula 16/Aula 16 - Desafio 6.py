# Tuplas & Váriaveis
words = ('aprender', 
        'programar', 
        'linguagem', 
        'python', 
        'curso',
        'gratis', 
        'estudar',
        'praticar',
        'trabalhar',
        'mercado',
        'programador',
        'futuro'
        )
postion = 0

for position in range(0, len(words)): #VOGAIS: a e i o u
    # Exibe a palavra que está sendo lida
    print(f'A palavra {words[position]} tem as vogais: ', end='')

    #Checa a primeira vogal
    if 'a' in words[position]:
        print('A', end=' ')
    
    #Checa a segunda vogal
    if 'e' in words[postion]:
        print('E', end=' ')
    
    #Checa a terceira vogal
    if 'i' in words[position]:
        print('I', end=' ')

    # Checa a quarta vogal
    if 'o' in words[position]:
        print('O', end=' ')

    # Checa a quinta e ultima vogal
    if 'u' in words[position]:
        print('U', end='')
    
    print()
    