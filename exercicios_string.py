# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

print ("******** Convertendo String para maisculas ********")

val_string = str(input("Digite a String Desejada:"))

print(val_string.upper())
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

print ("******** Convertendo String para minusculas ********")

val_string = input("Digite a String Desejada:")

print(val_string.lower())

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
print(" ******** Removendo espaços em branco de uma String ********")
frase= input("Insira uma frase: ")

print(frase.strip())
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
print(" ******** Informando data em string ********")

data_str = input("Digite uma data no formato dd/mm/aaaa: ")

print(data_str.split("/"))

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
print(" ******** Concatenando strings ******** ")
val_string1 = input("Insira uma palavra: ")
val_string2 = input("Insira outras palavra: ")

print(val_string1 + " " + val_string2 )