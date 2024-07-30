#Váriaveis & Listas
expression = 0
position = 0
open_parentheses_quantity = 0
closed_parentheses_quantity = 0
splited_expression = []

#Código
expression = input('Digite uma expressão que tenha PARÊNTESES: ') # Pergunta qual a expressão que o usuário que cehcar se é valida
while '(' not in expression and ')' not in expression: # Checa se o usuário digitou uma expressão qye tenha algum parenteses
    print('EXPRESSÃO INVÁLIDA')
    expression = input('Digite uma expressão que tenha PARÊNTESES ')
splited_expression = list(expression) # Divide a string em careacteres para a verificação se a exoressão é valida

for position in range(len(splited_expression)): # Checa a quantidade de parentêses que abre "(" e que feccha ")"
    if splited_expression[position] == ')' and open_parentheses_quantity == 0:
        open_parentheses_quantity += 5
        break
    elif '(' in splited_expression[position]: #Cehca se na posição está o parentêses que abre "("
        open_parentheses_quantity += 1
    elif ')' in splited_expression[position]: #Checa se na posição está o parntêses que fecha ")"
     closed_parentheses_quantity += 1

if open_parentheses_quantity == closed_parentheses_quantity:
    print('Esta operação é válida!')
else:
    print('Infelizmente, esta operação é inválida.')
