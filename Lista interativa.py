#Programa que cria uma lista onde você pode apagar, adicionar e listar.

lista = []
lista_tamanho = len(lista)



while True:
    
    tecla_apertada = input("Selecione uma opção \n [i]nserir  [a]pagar  [l]listar: " )

    if tecla_apertada == "i":
        item_adicionar = input("Digite O item que deseja adicionar: ")
        lista.append(item_adicionar)
        lista_tamanho += 1


    elif tecla_apertada == "a":
        item_para_apagar = input('Digite o numero do item no qual deseja apagar: ')
        int_apagar = int(item_para_apagar)
        
        for valor, compra in enumerate(lista):
            if valor == int_apagar:
                print("Removido com Sucesso!")
                del lista[valor]
                lista_tamanho -= 1
                break
            
        else:
            print("Este valor não existe")

            

    elif tecla_apertada == "l":
        
        if lista_tamanho == 0:
            print("Nada para listar")

        elif lista_tamanho >= 1:
            for indice, item in enumerate(lista):
                print(f'{indice} --- {item}')

    else:
        print("VOCÊ NÃO DIGITOU UMA TECLA CORRETA")
    