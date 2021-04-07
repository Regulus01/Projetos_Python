import PySimpleGUI as sg


def Esconde_Letras(Acertos, Nome_Escolhido):
    Acertos += Nome_Escolhido      #adiciona o nome escolhido na lista de acertos e separa as letras
    for k in range(len(Acertos)):  #percorre a lista de acertos de acordo com a separação da palavra
        Acertos[k] = '❏'           #troca todas as letras por ''❏''


def janela_jogo():
    sg.theme('Reddit')
    layout = [[sg.Text('Digite uma letra'), sg.Input(k='-IN-'), sg.Button('OK')],
              [sg.Output(size=(80, 20), key='-OUTPUT-')],
              [sg.Text('\t\t\t\t\t\t\t\t\t'), sg.Button('Voltar')]]
    return sg.Window('Forca new era', layout=layout, finalize=True)


def procurar_letra(Tema, Digitadas1, ContAcertos):
    for i in range(len(Tema)):  # percorre a lista do nome escolhido e conta as letras
        if Digitadas1 == Tema[i]:  # verifica se a lista 'Digitadas' tem letras do 'Palavra_Chave'
            ContAcertos[i] = Digitadas1  # Acertos recebe se a letra estiver no nome escolhido e os ❏ são trocados
            if Digitadas1 not in ContAcertos:
                ContAcertos.append(Digitadas1)


def janela_principal():
    sg.theme('Reddit')
    layout = [[sg.Text('\t\t\tSelecione o Tema')], [sg.Text('')],
              [sg.Button('Nomes'), sg.Button('Frutas'),
               sg.Button('Carros'), sg.Button('Aleatorio'), sg.Button('Anime'),
               sg.Button('Jogos'), sg.Button('Limpar-Tema')],
              [sg.Text('Selecione a quantidade de erros:')], [sg.Button('3'), sg.Button('6')],
              [sg.Text('\t\t\t'), sg.Button('Jogar')],
              [sg.Text('\t\t\t\t\t\t\t'), sg.Button('Sair')]]
    return sg.Window('Forca new era', layout=layout, finalize=True)


def Trocar_Quadrado(Acertos, Nome_Escolhido):
    Acertos += Nome_Escolhido  # adiciona o nome escolhido na lista de acertos e separa as letras
    for k in range(len(Acertos)):  # percorre a lista de acertos de acordo com a separação da palavra
        Acertos[k] = '❏'


def Boneco_Cont_Erros(Digitadas1, Digitadas, Tema, ContaErros, Erros, ContAcertos, window):
    z = '-' * 5
    q = ' - '
    if Digitadas1 in Digitadas:
        print('\nLetra repetida!')
    elif Digitadas1 not in Tema:
        print('\nNão tem essa letra na palavra!')
        ContaErros += 1
    if ContaErros == 1 and Erros == 3:
        window['-OUTPUT-'].update('Palavra:', {ContAcertos}, {len(ContAcertos)}, 'Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|  '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 2 and Erros == 3:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|             '
              '\n|')
    if ContaErros == 3 and Erros == 3:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|        / \  '
              '\n|')
    if ContaErros == 1 and Erros == 6:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|          '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 2 and Erros == 6:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /  '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 3 and Erros == 6:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|  '
              '\n|            '
              '\n|           '
              '\n|')

    if ContaErros == 4 and Erros == 6:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 5 and Erros == 6:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|          '
              '\n|')
    if ContaErros == 6 and Erros == 6:
        window['-OUTPUT-'].update(f'Palavra: {ContAcertos} \n{len(ContAcertos)} Letras')
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|        / \  '
              '\n|')


def Inicio_Jogo(ContAcertos):
    z = '-' * 5
    q = ' - '
    print(f'\n{z}Inicio do jogo{z}!')
    print(f'Palavra: {q.join(ContAcertos)} \n{len(ContAcertos)} Letras')
    print(' ____________'
          '\n/                     |'
          '\n|          '
          '\n|           '
          '\n|            '
          '\n|          '
          '\n|')