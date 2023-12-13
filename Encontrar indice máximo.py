# Atividade: Encontre o Índice Máximo
# Dada uma lista de números inteiros, escreva 
#um programa em Python que encontre e 
# imprima o índice do elemento máximo na lista.
# ] Não use a função enumerate() para esta atividade. 
# Em vez disso, utilize a função range() e um loop for.

lista = [12, 45, 89, 6, 23, 67, 91, 53]
maximo = lista[0]  # Assumimos que o primeiro elemento é o máximo
indice_maximo = 0  # Inicializamos o índice máximo como 0

for indice in range(1, len(lista)):
    if lista[indice] > maximo:
        maximo = lista[indice]
        indice_maximo = indice

print(f"O elemento máximo {maximo} está no índice {indice_maximo}")
