# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

print("******Exercicio de adição +******")
valor1= float(input("Insiria o primeiro valor: "))
valor2 = float (input("Insira o segundo valor: "))
resultado_adicao = valor1 + valor2

print(f"O resultado da adição do {valor1} e do {valor2} é de: {resultado_adicao}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
print("******** Calculo da media ********")
med_1 = float(input("Insira o primeir valor:"))
med_2 = float(input("Insira o segundo valor para calcular a media: "))

media = (med_1 + med_2)  / 2

print(f"A media é dos valores {med_1} e {med_2} é: {media}")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

print("******** Calculando potencia de um numero float ******** ")
val_base = float(input("Digite o valor base para o calculo da potencia: "))
val_expoente = float(input("Digite o valor do expoente:"))

val_potencia = val_base ** val_expoente

print (f"O resultado da potencia do numero {val_base} com o expoente {val_expoente} é: {val_potencia}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
print(" ******** Convertendo Temperatura Celcius para Fahrenheit ********")

celcius= float(input("Por favor diga qual é a temperatura: "))

fahrenheint = (celcius * 9/5) + 32


print (f"A temperatura de Celsios {celcius}ºC convertida para Fahrenheit é de {fahrenheint}ºC graus")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

print("******** Exercicio Calcular Area de um circulo ********")

raio = float(input("Por favor informe o raio para o calculo da Area do Circulo:"))
constante_cir = 3.14159
potencia = raio ** 2
area_circulo= constante_cir * potencia

print (f" A area do circulo com base no raio {raio} informado é de {area_circulo} cm²")