#  Exercicios Inteiros

#Escreva um programa que soma dois números inteiros inseridos pelo usuário.

print("Exercicio de soma de inteiros!!")

valor1 = int(input("Insira o primeiro valor da soma: "))
valor2 = int(input("Insira o segundo valor da soma: "))

soma = valor1 + valor2

print(f"O resultado da soma dos dois numeros é de: {soma}")

#Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

print( "Exercicio de Resto da Divisão(modulo) % ")

div_valor = int(input("Digite o valor que sera utilizado para calcular o resto da divisão:"))
rest_div = 5
resul_div = div_valor % rest_div

print (f"O resto da divisão é {resul_div}")

#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

print ("Exercicio de multiplicação * ")

num1 = int(input("Digite o primeiro valor a ser multiplicado: "))
num2 = int (input("Digite o segundo valor que sera multiplicado: "))

multiplica = num1 * num2

print(f"O resultado da multiplicação é de: {multiplica}")

#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

print("Exercicio de divisão inteira / ")

div1 = int(input("Digite o valor a ser dividido: "))
div2 = int (input("Digite por qual valor ele sera dividido: "))

div_resul = div1 // div2

print(f"O resultado da divisão de {div1} por {div2} é de: {div_resul}")

#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

print("Calcudo do Quadrado ** ")


valor_qua = int(input("Insira o valor que você quer elevar ao quadrado: "))

quadrado = valor_qua ** 2

print(f" O quadrado de {valor_qua} é de: {quadrado}")