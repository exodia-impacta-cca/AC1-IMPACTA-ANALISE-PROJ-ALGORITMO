def busca_linear(lista, numero_procurado):
    elemento = []
    for i in range(len(lista)):
        if lista[i] == numero_procurado:
            elemento.append(i)
    return elemento

lista = [32, 35, 65, 4, 4, 98, 29, 33, 18, 82, 74, 63, 57, 2, 1, 30]
print(lista)
numero_procurado = int(input("Digite o número que deseja procurar na lista: "))

resposta = busca_linear(lista, numero_procurado)
print("O número procurado está presente no(s) elemento(s):", resposta)