# Tupla & Variáveis
words = (
    'aprender',
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
position = 0

# Código
for position in range(0, len(words)):
    print(f'A palavra {words[position]} tem as vogais: ',end='')

    #Checa a primeira vogal
    if 'a' in words[position]:
        print('A', end=' ')
    
    #Checa a segunda vogal
    if 'e' in words[position]:
        print('E', end=' ')

    #Checa a terceira vogal
    if 'i' in words[position]:
        print('I', end=' ')
    
    #Checa a quarta vogal
    if 'o' in words[position]:
        print('O', end=' ')
    
    #Checa a quinta e última vogal
    if 'u' in words[position]:
        print('U', end=' ')
    
    print()


# GUANABRA MASTER RESOLUTION
# palavars = (
#     'aprender',
#     'programar',
#     'linguagem',
#     'python',
#     'curso',
#     'gratis',
#     'estudar',
#     'praticar',
#     'trabalhar',
#     'mercado',
#     'programador',
#     'futuro'
#         )
# for p in palavras: "p' vai ser a palavra que o código ta lendo
# print(f'na palabra {p} temos: ') <-- exibie a palavra que está sendo analisada
# for letra in p: <-- palavras são listas, então ele vai ler cada lista(letra) da palavra sendo analisada
# if letra in 'aeiou':
# print(letra, end='') <-- desse jeito ele vai analisar letra por letra, e se tiver uma vogal repetida ele vai exibir no terminal