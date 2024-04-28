# Tuplas & Variáveis
teams = ('Botafogo',
         'Atlético Mineiro',
         'Bragantino',
         'Bahia',
         'Flamengo',
         'Atlético Paranaensa',
         'Internacional',
         'Cricíuma',
         'Fluminense',
         'Cruzeiro',
         'Fortaleza',
         'Palmeiras',
         'Juventude',
         'São Paulo',
         'Vasco da Gama',
         'Esporte Clube Vitória',
         'Corinthians',
         'Atlético Goianiense',
         'Cuiabá'
         )
sorted_teams = ''
teams_count = 0

# Código
print('DIA 28/04/2024')
print(f'Os 5 primeiros colocados do brasileirão são: ', end=' ') 

while teams_count != 5:
    print(teams[teams_count], end=' ')
    teams_count += 1
teams_count = 0

print()
print('-=-' * 32)

print('Ultimos 4 colocados do brasileirão: ')
while teams_count != 4:
    print(teams[-teams_count -1], end=' ')
    teams_count += 1
teams_count = 0

print()
print('-=-' * 32)
sorted_teams = sorted(teams)

print('Times em ordem alfabética: ')
for teams_count in range(0, len(teams)):
    print(sorted_teams[teams_count], end=' ')
teams_count = 0

print()
print('-=-' * 32)

print('Chapecoense não está na série A esse ano.')
