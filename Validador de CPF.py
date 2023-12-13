# Programa para validar cpf, 
# após digitar irá fazer o calculo, vai ser capaz de saber se
# o primeiro digito é o correto.

cpf = input("Digite seu CPF:  ")\
    .replace(".", "") \
    .replace(" ", "") \
    .replace("-", "") \
    
cpf_novo = ""
cpf_soma = []
indice_base = 0
valor_a_multiplicar = 10
resultado = ""
primeiro_digito = ""

for i, valor in enumerate(cpf):

    if valor != "." and valor != "-":
        cpf_novo += valor + ""



for indice, caracter in enumerate(cpf_novo):
    if valor_a_multiplicar >= 2:
        if caracter != "." and caracter != "-":
            if indice == indice_base:
                resultado = int(caracter) * valor_a_multiplicar
                cpf_soma.append(resultado,)
                indice_base += 1
                valor_a_multiplicar -= 1

soma_final = sum(cpf_soma) * 10 % 11


if soma_final > 9:
    primeiro_digito = 0
else:
    primeiro_digito = soma_final

print(f'O primeiro digito do CPF é: {primeiro_digito}')






    


            





            


#        print(int(caracter))