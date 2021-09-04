from geradorAleatorios import l1,l2,l3

# implementação do algoritmo bubble-sort
def bubbleSort(lista):
    for i in range(len(lista)-1,0,-1):
        for j in range(i):
            if lista[j]>lista[j+1]:
                lista[j] ,lista[j+1] = lista[j+1], lista[j]
        print(lista)
                
                
# Testes do algoritmo bubble-sort
# l1 Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]
print('lista Aleatória:')
print(l1)

print('lista em processo processo de Ordenação:')
bubbleSort(l1)

print('lista Ordenada:')
print(l1)
