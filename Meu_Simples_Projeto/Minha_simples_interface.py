import PySimpleGUI as sg
import random
# algoritmos de ordenacao
import Bubble_sort as bs
import strand_sort as ss
import selection_sort as sels
import Insertion_Sort as iser

import timeit

lista_numeros = []

sg.theme('dark grey 9')
layout = [[sg.Text('Digite os Números:'), sg.Input(k='-IN-')],
          [sg.Button('OK')],
          [sg.Text('\t\tSelecione o método de ordenação')],
          [sg.Text('')],
          [sg.Button('Bubble-Sort'), sg.Button('Strand-Sort'),
           sg.Button('Selection-Sort'), sg.Button('Insertion-Sort'), sg.Button('Limpar-Lista'),
           sg.Button('Numeros-Aleatorios')],
          [sg.Text('')], [sg.Output(size=(80, 5), key='-OUTPUT-')], [sg.Button('Sair')]]


window = sg.Window('Métodos de ordenação', layout)

while True:
    event, values = window.read()
    if event == 'OK':
        try:
            lista_numeros += [int(values['-IN-'])]
            window['-OUTPUT-'].update(lista_numeros)
        except ValueError:
            sg.Popup('Valor não adicionado, Digite apenas um valor do tipo inteiro')

    if event == 'Bubble-Sort':
        contador = 0
        point_1 = timeit.default_timer()
        bs.bubble_sort(lista_numeros, contador)
        point_2 = timeit.default_timer()
        delta = (point_2 - point_1) * 10 ** 9
        window['-OUTPUT-'].update(lista_numeros)
        print('')
        print('')
        print(f'Numeros Ordenados com o bubble sort, Duração: {delta:.0f} nanosegundos')
    elif event == 'Limpar-Lista':
        lista_numeros.clear()
        window['-OUTPUT-'].update(f'Seus numeros Digitados foram limpos, a lista agora contem {len(lista_numeros)} '
                                  f'numeros')
    elif event == 'Strand-Sort':
        contador = 0

        point_1 = timeit.default_timer()
        lista_3 = ss.StrandSort(lista_numeros)
        point_2 = timeit.default_timer()
        delta = (point_2 - point_1) * 10 ** 9
        window['-OUTPUT-'].update(lista_3)

        print('')
        print('')
        print(f'Numeros Ordenados com o Strand sort, Duração: {delta:.0f} nanosegundos')

    elif event == 'Selection-Sort':
        point_1 = timeit.default_timer()
        sels.selection_sort(lista_numeros)
        point_2 = timeit.default_timer()
        delta = (point_2 - point_1) * 10 ** 9
        window['-OUTPUT-'].update(lista_numeros)
        print('')
        print('')
        print(f'Numeros Ordenados com o Selection Sort, Duração: {delta:.0f} nanosegundos')

    elif event == 'Insertion-Sort':
        point_1 = timeit.default_timer()
        iser.insertion_sort(lista_numeros)
        point_2 = timeit.default_timer()
        delta = (point_2 - point_1) * 10 ** 9
        window['-OUTPUT-'].update(lista_numeros)
        print('')
        print('')
        print(f'Numeros Ordenados com o Insertion Sort, Duração: {delta:.0f} nanosegundos')

    elif event == 'Numeros-Aleatorios':
        for k in range(0, 20):
            numero = random.randint(1, 2000)
            lista_numeros.append(numero)
        window['-OUTPUT-'].update(lista_numeros)
    elif event == 'Sair' or event == sg.WIN_CLOSED:  # cria o evento de saida
        break

window.close()
