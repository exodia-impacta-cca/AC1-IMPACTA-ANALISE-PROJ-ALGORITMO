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

print(geradorAleatorios())
print(geradorAleatorios())
print(geradorAleatorios())

# [32, 35, 65, 4, 4, 98, 29, 33, 18, 82, 74, 63, 57, 2, 1, 30]
# [93, 37, 53, 97, 75, 28, 44, 60, 89, 0, 58, 95, 56, 32, 38, 14]
# [37, 40, 70, 58, 26, 12, 69, 33, 9, 92, 14, 4, 24, 66, 23, 92]