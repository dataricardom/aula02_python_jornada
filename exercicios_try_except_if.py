# #### try-except e if

# 21: Conversor de Temperatura
# print("********** Conversor de Temperatura **********")

# try:
#     celcius = float(input("Insira a temperatura:"))
#     fahrenheint = (celcius * 9/5) + 32
#     print (f"A temperatura de {celcius} graus celcius convertida para fahrentheint é de : {fahrenheint} graus")
# except ValueError:
#     print ("Digite uma temperatura valida")


# 22: Verificador de Palíndromo
print("************ Verificador de Palidromo **********")
palidromo = input("Digite a palavra que deseja verificar se é Palidromo: ")
try:
    if isinstance(palidromo, str):
    
        formatado = palidromo.replace(" ", "").lower()
        if formatado == formatado[::-1]:
            print("A palavra ou frase informada é um palidromo")
        else:
            print("Não é um palidromo")
    else:
        print("Entrada inválida. Digite uma palavra ou frase")
except ValueError:
    print("Por favor digite uma string")
# 23: Calculadora Simples

# print("************ Calculadora Simples **********")
# print("Seleciona a operação")
# print ("1 - Adição (+)")
# print ("2 - Subtração (-)")
# print ("3 - Multiplicação (*)")
# print ("4 - Divisão (/)")

# operacao = input("Por favor digita qual operação sera realizada: 1, 2 , 3 , 4: ")

# if operacao in ['1','2','3','4']:
    
#     try:
#         num1 = float(input("Digite o primeiro numero: "))
#         num2 = float(input("Digite o segundo numero: "))

#         if operacao == "1":

#             result1 = num1 + num2
#             print(f"{num1} + {num2} =  {result1}")

#         elif operacao == "2":

#             result2 = num1 - num2
#             print(f"{num1} - {num2} = {result2}")

#         elif operacao == "3":

#             result3 = num1 * num2
#             print(f"{num1} * {num2} = {result3}")

#         elif operacao == "4" and num2 != 0:
            
#             result4 = num1 / num2   
#             print(f"{num1} / {num2} = {result4}")
#         else:
#                 print("Erro: Divisão por zero não é permitida.")
#     except ValueError:

#         print("Erro: Entrada invalida. Informe apenas números")

# else:

#     print("Operação inválida. Por favor, escolha entre 1,2,3 ou 4.")

# 24: Classificador de Números

# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

# 25: Conversão de Tipo com Validação

# entrada_lista = input("Digite uma lista de números separados por vírgula: ")
# numeros_str = entrada_lista.split(",")
# numeros_int = []
# try:
#     for num in numeros_str:
#         numeros_int.append(int(num.strip()))
#     print("Lista de inteiros:", numeros_int)
# except ValueError:
#     print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")