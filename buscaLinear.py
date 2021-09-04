from geradorAleatorios import l1,l2,l3

# Implementação do algoritmo de busca linear
def busca_linear(lista, numero_procurado):
    for i in range(len(lista)):
        if lista[i] == numero_procurado:
            return True
    return False


# Testes do algoritmo de busca linear
print(l1)
numero_procurado = int(input("Digite o número que deseja procurar na lista: "))

if busca_linear(l1, numero_procurado):
    print('Número encontrado!')
else:
    print('Não está na lista!')
