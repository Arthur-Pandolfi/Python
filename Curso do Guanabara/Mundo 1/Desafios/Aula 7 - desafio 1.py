a1 = int(input('Digite um valor: '))
a2 = int(input('Digite outro valor: '))
multi = a1 * a2
soma = a1 + a2
divisaonormal = a1 / a2
divisaointeira = a1 // a2
divisaoresto = a1 % a2
potencia = a1 ** a2
print('O valor da soma é {},O produto é {},A divisão é {:.3f}.'.format(soma,multi,divisaonormal), end='>>>')
print('O valor do inteiro da divisão é {},O valor do resto da divisão é {:.3f},E a potencia é {}'.format(divisaointeira,divisaoresto, potencia))
#\n = Quebrar linha
#{:.3f} quantidade de números decimais dentro de um "Format"
#end='O que ter no final da linha'
