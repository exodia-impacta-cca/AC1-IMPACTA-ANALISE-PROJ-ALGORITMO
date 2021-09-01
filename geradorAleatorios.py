# Gerador de sequencias de numeros aleatórios para usar como entrada para os métodos de ordenação.
import random

def geradorAleatorios():
    listaNaoOrdenada = []
    
    # Tamanho da lista, conforme professor solicitou
    tamanhoLista = 15
    
    # Gera lista com numeros aleatórios e adiciona a lista
    for i in range(tamanhoLista):
        listaNaoOrdenada.append(random.randint(0,99))
    return listaNaoOrdenada

print(geradorAleatorios())