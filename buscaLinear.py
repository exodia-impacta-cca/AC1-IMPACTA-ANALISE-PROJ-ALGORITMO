from geradorAleatorios import l1,l2,l3

# Implementação do algoritmo de busca linear
def busca_linear(lista, numero_procurado):
    elemento = []
    for i in range(len(lista)):
        if lista[i] == numero_procurado:
            elemento.append(i)
    return elemento


# Testes do algoritmo de busca linear
print(l1)
numero_procurado = int(input("Digite o número que deseja procurar na lista: "))
resposta = busca_linear(l1, numero_procurado)
if len(resposta) > 1:
    print("O número procurado está presente na(s) posição(ões):" + str(resposta) + " da lista.")
else:
    print("O número não foi encontrado!")