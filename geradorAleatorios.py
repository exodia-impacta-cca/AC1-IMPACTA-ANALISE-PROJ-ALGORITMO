# Gerador de sequencias de numeros aleatórios para usar como entrada para os métodos de ordenação.
import random

def geradorAleatorios():
    listaNaoOrdenada = []
    
    # Tamanho da lista, conforme professor solicitou
    tamanhoLista = 16
    
    # Gera lista com numeros aleatórios e adiciona a lista
    for i in range(tamanhoLista):
        listaNaoOrdenada.append(random.randint(0,99))
    return listaNaoOrdenada

# Listas em ordenação aleatória e ordenada

# Aleatória
l1 = [32, 35, 65, 4, 4, 98, 29, 33, 18, 82, 74, 63, 57, 2, 1, 30]
# Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]

# Aleatória
l2 = [93, 37, 53, 97, 75, 28, 44, 60, 89, 0, 58, 95, 56, 32, 38, 14]
# Ordenada
# [0, 14, 28, 32, 37, 38, 44, 53, 56, 58, 60, 75, 89, 93, 95, 97]

# Aleatória
l3 = [37, 40, 70, 58, 26, 12, 69, 33, 9, 92, 14, 4, 24, 66, 23, 92]
# Ordenada
# [4, 9, 12, 14, 23, 24, 26, 33, 37, 40, 58, 66, 69, 70, 92, 92]


