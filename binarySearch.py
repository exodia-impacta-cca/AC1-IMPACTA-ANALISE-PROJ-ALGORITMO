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

lista = [0, 14, 28, 32, 37, 38, 44, 53, 56, 58, 60, 75, 89, 93, 95, 97]
print(lista)
numero_procurado = int(input("Digite o número que deseja procurar na lista: "))

resposta = busca_binaria(lista, numero_procurado)
print("O número procurado está presente na lista?", resposta)