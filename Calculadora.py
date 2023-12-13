#Calculadora 
while True:

    numero_1 = input("Digite seu Primeiro numero: ") 
    operador = input("Digite o Operador (+-/*): ")
    numero_2 = input("Digite seu Segundo numero: ")

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
        
    except:
        numeros_validos = None

    if numeros_validos is None:
        print("Um ou Ambos os numeros digitados são INVÁLIDOS.")
        continue

    operadores_permitidos = "+-/*"

    if len(operador) > 1:
        print("Digite somente 1(quantidade) de Operador")
        continue


    if operador not in operadores_permitidos:
        print("Operador INVÁLIDO")
        continue

    print ("Realizando Sua Conta")
    if operador == "+":
        print(num_1_float + num_2_float)

    elif operador == "-":
        print(num_1_float - num_2_float)

    elif operador == "/":
        print(num_1_float / num_2_float)

    elif operador == "*":
        print(num_1_float * num_2_float)

    else:
        print("Nunca deve chegar aqui")

    sair = input("Quer sair? [s]im: ").lower().startswith("s")
    print(sair)
    
    if sair is True:
        break