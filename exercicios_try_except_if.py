# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples

print("************ Calculadora Simples **********")
print("Seleciona a operação")
print ("1 - Adição (+)")
print ("2 - Subtração (-)")
print ("3 - Multiplicação (*)")
print ("4 - Divisão (/)")

operacao = input("Por favor digita qual operação sera realizada: 1, 2 , 3 , 4: ")

if operacao in ['1','2','3','4']:
    
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        if operacao == "1":

            result1 = num1 + num2
            print(f"{num1} + {num2} =  {result1}")

        elif operacao == "2":

            result2 = num1 - num2
            print(f"{num1} - {num2} = {result2}")

        elif operacao == "3":

            result3 = num1 * num2
            print(f"{num1} * {num2} = {result3}")

        elif operacao == "4" and num2 != 0:
            
            result4 = num1 / num2   
            print(f"{num1} / {num2} = {result4}")
        else:
                print("Erro: Divisão por zero não é permitida.")
    except ValueError:

        print("Erro: Entrada invalida. Informe apenas números")

else:

    print("Operação inválida. Por favor, escolha entre 1,2,3 ou 4.")

# 24: Classificador de Números
# 25: Conversão de Tipo com Validação