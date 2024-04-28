times_em_ordem = (
                    "Bragantino", #1
                    "Flamengo", #2
                    "Botafogo", #3
                    "Atlético Paranaense", #4
                    "Grêmio", #5
                    "Internacional", #6
                    "Atlético Mineiro", #7 
                    "Fortaleza", #8
                    "Bahia", #9
                    "Fluminense", #10
                    "Palmeiras", #11
                    "Cruzeiro", #12
                    "Juventude", #13
                    "São Paulo", #14
                    "Vasco da Gama", #15
                    "Cricíuma", #16
                    "Esporte Clube Vitória", #17
                    "Corinthians", #18
                    "Atlético Goianiense", #19
                    "Cuiabá", #20
                )
print('5 primeiros colocados: ')
for c in times_em_ordem[:5]:
    print(c)
del(c)

print("-" * 50)

print('Os últimos 4 colocados: ')
for c in times_em_ordem[16:]:
    print(c)
del(c)

print("-" * 50)

print("Tabela em ordem alfabética: ")

times_em_ordem_atualizado = sorted(times_em_ordem)
for c in times_em_ordem_atualizado:
    print(c)

print("-" * 50)

if "Chapecoense" in times_em_ordem:
    print("O time chapecoense está participando.")
else:
    print("O time chapecoense não está participando")
    


