from geradorAleatorios import l1,l2,l3

# Implementação do algoritmo de busca binária
def busca_binaria(lista, numero_procurado):
    primeiro = 0
    ultimo = len(lista) - 1
    while primeiro <= ultimo:
        meio = ((primeiro + ultimo) // 2)
        if lista[meio] == numero_procurado:
            return True
        else:
            if numero_procurado < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return False


# Testes do algoritmo de busca binária
# Ordena a lista antes de realizar a busca binária
l1.sort()
print(l1)
numero_procurado = int(input("Digite o número que deseja procurar na lista: "))

resposta = busca_binaria(l1, numero_procurado)
print("O número procurado está presente na lista?", resposta)
