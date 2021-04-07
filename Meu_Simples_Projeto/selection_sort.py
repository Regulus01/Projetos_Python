def selection_sort(numeros):
    for index in range(0, len(numeros)):
        min_index = index  # pra cada posição grava o numero minimo
        for right in range(index + 1, len(numeros)):
            # percorre o resto do array procurando o item minimo
            if numeros[right] < numeros[min_index]:
                min_index = right  # quando achar o menor item associa ele com a variável
        # no final faz a troca
        numeros[index], numeros[min_index] = numeros[min_index], numeros[index]
