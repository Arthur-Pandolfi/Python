a = str(input('Digite algo: '))
tipo = type(a)
espa = a.isspace()
letra = a.isalpha()
maiu = a.isupper()
minu = a.islower()
capi = a.istitle()
num = a.isnumeric()
lenu = a.isalnum()
print(f'Esses digitos são de que tipo? {tipo}\nSó tem espaços? {espa}\nSão só letras? {letra}'
      f'\nEstão escritas só em maiusculo? {maiu}\nEstão escritas são em minusculas? {minu}'
      f'\nEstão capitalizadas? {capi}\nSão só números? {num}\nSão alfas-numéricos? {lenu}')
