from geradorAleatorios import l1,l2,l3

# Implementação do algoritmo quick-sort **
def particiona(lista, comeco, fim):
    pivo = lista[fim]
    i = comeco-1
    for j in range(comeco, fim):
        if lista[j] < pivo:
            i = i+1
            lista[i], lista[j] = lista[j], lista[i]
    if pivo < lista[i+1]:
        lista[i+1], lista[fim] = lista[fim], lista[i+1]
    print(lista)
    return i+1

def quicksortIntermediario(lista, comeco, fim):
    if comeco < fim:
        p = particiona(lista, comeco, fim)
        quicksortIntermediario(lista, comeco, p-1)
        quicksortIntermediario(lista, p+1, fim)
        
def quicksort(lista):
    quicksortIntermediario(lista, 0, len(lista)-1)

# Testes do algoritmo quick-sort
# l1 Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]
print('Lista Aleatória:')
print(l1)

print('Lista em processo processo de Ordenação:')
quicksort(l1)

print('Lista Ordenada:')
print(l1)