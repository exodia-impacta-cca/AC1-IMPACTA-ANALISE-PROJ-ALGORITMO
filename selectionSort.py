from geradorAleatorios import l1,l2,l3
# Implementação do algoritmo selection-sort

def selectionSort(lista):
    n = len(lista)
    for i in range(n-2):
        minimo = i
        for  j in range(i+1,n):
            if lista[j] < lista[minimo]:
                minimo = j
        if i != minimo:
            lista[i], lista[minimo] = lista[minimo], lista[i]
        print(lista)
            

# l1 Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]
print('lista Aleatória:')
print(l1)

print('lista em processo processo de Ordenação:')
selectionSort(l1)

print('lista Ordenada:')
print(l1)
# Testes do algoritmo selection-sort