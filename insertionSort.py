from geradorAleatorios import l1,l2,l3
# Implementação do algoritmo insertion-sort

def insertionSort(lista):
    n = len(lista)
    for i in range(1,n):
        elemento = lista[i]
        j = i-1
        while ((j>=0)  and (elemento < lista[j])):
            lista[j+1] = lista[j]
            j = j-1
        lista[j+1] = elemento
        print(lista)
            
# Testes do algoritmo insertion-sort
# l1 Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]
print('lista Aleatória:')
print(l1)

print('lista em processo processo de Ordenação:')
insertionSort(l1)

print('lista Ordenada:')
print(l1)