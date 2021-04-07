# Utilizando o bubble sort


def bubble_sort(vector, contador):
    for k in range(0, len(vector)-1):
        if vector[k] > vector[k+1]:
            # troca a posição da variável auxiliar até que
            # ela seja maior que os elementos da posição anterior do vetor
            aux = vector[k]
            vector[k] = vector[k+1]
            vector[k+1] = aux
    if contador == len(vector):
        pass
    else:
        contador += 1
        bubble_sort(vector, contador)

