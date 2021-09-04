from geradorAleatorios import l1,l2,l3

# Implementação do algoritmo merge-sort
def mergeSort(lista):
    n = len(lista)
    if n == 1:
        return lista
    
    meio = len(lista)//2
    l1 = lista[:meio]
    l2 = lista[meio:]
    
    l1 = mergeSort(l1)
    l2 = mergeSort(l2)

    return mesclar(l1,l2)


def mesclar(a,b):
    c = []
    while ((len(a) > 0) and (len(b) > 0)):
        if a[0] > b[0]:
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    while (len(a) > 0):
        c.append(a[0])
        a.remove(a[0])
    while(len(b) > 0):
        c.append(b[0])
        b.remove(b[0])
    print(c)
    return c
                

# Testes do algoritmo merge-sort
# l1 Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]
# 1 metade: 32, 35, 65, 4, 4, 98, 29, 33
# 2 metade: 18, 82, 74, 63, 57, 2, 1, 30


print('Lista Aleatória:')
print(l1)

print('Lista em processo processo de Ordenação:')
l1 = mergeSort(l1)

print('Lista Ordenada:')
print(l1)