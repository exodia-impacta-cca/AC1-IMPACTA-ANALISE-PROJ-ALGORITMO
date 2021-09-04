from geradorAleatorios import l1,l2,l3

# Implementação do algoritmo bucket-sort
def bucketSort(arr, noOfBuckets):
    max_ele = max(arr)
    min_ele = min(arr)
 
    # range(for buckets)
    rnge = (max_ele - min_ele) / noOfBuckets
 
    temp = []
 
    # create empty buckets
    for i in range(noOfBuckets):
        temp.append([])
 
    # scatter the array elements
    # into the correct bucket
    for i in range(len(arr)):
        diff = (arr[i] - min_ele) / rnge - int((arr[i] - min_ele) / rnge)
 
        # append the boundary elements to the lower array
        if(diff == 0 and arr[i] != min_ele):
            temp[int((arr[i] - min_ele) / rnge) - 1].append(arr[i])
 
        else:
            temp[int((arr[i] - min_ele) / rnge)].append(arr[i])
 
    # Sort each bucket individually
    for i in range(len(temp)):
        if len(temp[i]) != 0:
            temp[i].sort()
 
    # Gather sorted elements
    # to the original array
    k = 0
    for lst in temp:
        if lst:
            for i in lst:
                arr[k] = i
                k = k+1
 

# Testes do algoritmo bucket-sort
# l1 Ordenada
# [1, 2, 4, 4, 18, 29, 30, 32, 33, 35, 57, 63, 65, 74, 82, 98]
print('Lista Aleatória:')
print(l1)

print('Lista em processo processo de Ordenação:')
bucketSort(l1, 5)

print('Lista Ordenada:')
print(l1)