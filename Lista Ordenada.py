def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1

numero_procurado = int(input("Digite o número que deseja procurar na lista: "))


numeros_ordenados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


posicao = busca_binaria(numeros_ordenados, numero_procurado)

if posicao != -1:
    print(f'O número {numero_procurado} está na posição {posicao} da lista.')
else:
    print(f'O número {numero_procurado} não está presente na lista.')