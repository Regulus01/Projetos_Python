import timeit
import time


def StrandSort(array):
    List = []
    while len(array) > 0:   # [5, 4, 1, 6, 8, 3, 15, -30, 1002]
        subarray = [array.pop(0)]

        x = 0
        while x < len(array):
            if array[x] > subarray[-1]: #se o array no primeiro caso pos 0 = 5 for maior que o ultimo numero da minha sublista
                                        # ela entra na minha sublista e é excluida do meu arrat
                subarray.append(array.pop(x))
            else:
                x = x + 1  # se não for, é adicionado +1 possição no meu x para percorrer meu array principal
        List = Merge(subarray, List)

    return List


def Merge(first, second):
    a = 0
    b = 0
    array_change = []

    while a < len(first) and b < len(second):
        if first[a] < second[b]:
            array_change.append(first[a])
            a += 1
        elif first[a] > second[b]:
            array_change.append(second[b])
            b += 1
        else:
            array_change.append(first[a])
            array_change.append(second[b])
            a += 1
            b += 1

    while a < len(first):
        array_change.append(first[a])
        a += 1

    while b < len(second):
        array_change.append(second[b])
        b += 1

    return array_change

