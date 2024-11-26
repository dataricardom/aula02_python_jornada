# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

expre_1 = True
expre_2 = False

result_bool = expre_1 and expre_2

print(f"O resultado da expressao é {result_bool}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

valor_1 = input("Insira o primeiro valor:")
valor_2 = input("Insira o segundo valor:")
# valor_1 = False
# valor_2 = True

valor_bool = valor_1 or valor_2

print(valor_bool)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

valor_4 = input("Insira um valor booleano")
inversao_valor = not valor_4
print(f"A inversão do valor boleano {valor_4} é {inversao_valor}")

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

numero_1 = input("Adicione o primeiro valor: ")
numero_2 = input("Adicione o segundo valor: ")

compara_valor = numero_1 == numero_2

print(f"O resultado da comparação é {compara_valor}")


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

numero_1 = input("Adicione o primeiro valor: ")
numero_2 = input("Adicione o segundo valor: ")

compara_valor = numero_1 != numero_2

print(f"Os numeros são diferentes? {compara_valor}")
