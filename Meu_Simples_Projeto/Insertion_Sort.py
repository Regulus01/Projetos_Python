def insertion_sort(Vetor):
    for k in range(1, len(Vetor)):
        # atribui os elementos da posição 1 a ultima posição da lista
        # toda vez que o for é executado no range de k
        elemento_corrente = Vetor[k]
        i = k - 1  # o i recebe a posição de k -1 ou seja quando k for 4 o i será == 3
        while i >= 0:
            if elemento_corrente < Vetor[i]:
                # se o elemento corrente for menor que o vetor pos [i]
                Vetor[i+1] = Vetor[i]
                Vetor[i] = elemento_corrente
                # ocorre a substituição do item na lista seguindo a posição do i
                # até que os itens estejam ordenados seguindo a condição do if
                i -= 1
            else:
                break
