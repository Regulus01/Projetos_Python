import PySimpleGUI as sg
from random import choice
import Funcoes

lista_numeros = []

# PALAVRAS CHAVES DA FORCA
Nomes = ['IURI', 'RODNEY', 'IAGO', 'JOSE', 'ANA', 'CAIO', 'ANDRE', 'LUCAS', 'PEDRO', 'PAULA', 'IGOR', 'DAVI', 'EDSON',
         'LAURA', 'LAILA', 'CHARLES', 'HUMBERTO', 'VICTOR', 'JAILTON', 'MATHEUS', 'ADRIANO']
Anime = ['FULLMETALALCHEMIST', 'BOKUNOHERO', 'DRAGONBALLZ', 'SAINTSEIYA', 'DIGIMON', 'YUGIOH', 'FATE', 'BLUEEXORCIST',
         'HAIUKYUU', 'BAKUGAN', 'POKEMON', 'SWORDARTONLINE', 'OVERLORD', 'HIGHSCHOLLOFTHEGOD', 'BTOOM', 'TOKYOGHOUL',
         'FIREFORCE', 'EDWARD', 'MIDORYA', 'YUGI', 'SEIYA', 'ALLMIGHT', 'SAIKI', 'GOKU', 'NARUTO', 'RIN', 'ALPHONSE',
         'SAITAMA']
Jogos = ['DARKSOULS', 'CYBERPUNK', 'THEWITCHER', 'SMASHBROS', 'MARIO', 'MORTALKOMBAT', 'RUNESCAPE', 'WARCRAFT', 'GTA'
         'THELEGENDOFZELDA', 'OUTLAST', 'NEWWORLD', 'LEAGUEOFLEGENDS', 'SMITE', 'DESTINY', 'GODOFWAR', 'SPIDERMAN']
Frutas = ['LARANJA', 'ABACAXI', 'MARACUJA', 'BANANA', 'AMORA', 'MANGA', 'ABACATE', 'GOIABA', 'MARMELO', 'UVA', 'JACA',
          'MELANCIA', 'TANGERINA', 'MAMAO', 'COCO', 'CARAMBOLA', 'BLUEBERRY', 'TOMATE', 'GRAVIOLA']
Carros = ['CHEVROLET', 'ONIX', 'PRISMA', 'FERRARI', 'BUGATTI', 'CAMARO', 'BMW', 'GOL', 'CROSSFOX', 'CORSA', 'TESLA']

Aleatorio = Nomes + Anime + Frutas + Carros + Jogos
Temas = ['Nomes', 'Frutas', 'Carros', 'Aleatorio', 'Anime', 'Jogos']
Lista_Palavras = [Nomes, Frutas, Carros, Aleatorio, Anime, Jogos]

#Contadores
Tema = []
Digitadas = []
ContaErros = 0
ContAcertos = []
Erros = 0
Acertos = 0
janela_principal, janela_jogo = Funcoes.janela_principal(), None

Tema_Temp = []


while True:
    window, event, values = sg.read_all_windows()
    try:
        for k in range(0, 6):
            if event in Temas[k]:
                Tema += choice(Lista_Palavras[k])
                Tema_Temp += ["".join(Tema)]
                sg.popup('Tema Selecionado')
    except TypeError:
        pass

    if window == janela_principal and event == 'Jogar' and Erros >= 3 and len(Tema) >= 1:
        janela_jogo = Funcoes.janela_jogo()
        Funcoes.Trocar_Quadrado(ContAcertos, Tema)
        Funcoes.Inicio_Jogo(ContAcertos)
        janela_principal.hide()

    if len(Tema_Temp) > 1:
        sg.popup('Você já escolheu um tema, o tema sera deletado')
        Tema.clear()
        Tema_Temp.clear()

    elif event == 'Limpar-Tema':
        sg.popup('Tema selecionado limpo')
        del Tema_Temp[0]
        del Tema[0]

    if event == '3':
        Erros = 3
        sg.popup('Quantidade de erros selecionada', Erros, button_color= 'Green')
    if event == '6':
        Erros = 6
        sg.popup('Quantidade de erros selecionada', Erros, button_color= 'Green')

    elif window == janela_jogo and event == 'Voltar':
        janela_jogo.hide()
        janela_principal.un_hide()

    if window == janela_jogo and event == 'OK':
        Digitadas1 = (str(values['-IN-'].upper()))

        for i in range(len(Tema)):  # percorre a lista do nome escolhido e conta as letras
            if Digitadas1 == Tema[i]:  # verifica se a lista 'Digitadas' tem letras do 'Palavra_Chave'
                ContAcertos[i] = Digitadas1  # Acertos recebe se a letra estiver no nome escolhido e os ❏ são trocados
                Acertos += 1
                if Digitadas1 not in ContAcertos:
                    ContAcertos.append(Digitadas1)
        if Digitadas1 in Digitadas:
            print('\nLetra repetida!')
        if Digitadas1 not in Tema:
            print('\nNão tem essa letra na palavra!')
            ContaErros += 1
            print(ContaErros, 'Contador erros')

        Funcoes.Boneco_Cont_Erros(Digitadas1, Digitadas, Tema, ContaErros, Erros, ContAcertos, window)

        q = " - "
        x = " "
        if Tema == ContAcertos:
            sg.popup(f'\nVocê ganhou!\n Palavra: {Tema} ')

        if ContaErros == Erros:
            sg.popup(f'\nVocê errou {ContaErros} vezes então perdeu o jogo \nA palavra era {q.join(Tema)}')

        print(f'Letras usadas: {x.join(Digitadas)} '
              f'\nAcertos: {Acertos} \nErros: {ContaErros} \n {q.join(ContAcertos)}')

    if event == 'Limpar-Tema':
        Tema.clear()
        Tema_Temp.clear()

    if event == 'Jogar' and (Erros < 3 or len(Tema) < 1):
        print(True)
        sg.popup('Selecione o tema e a quantidade de erros')

    if event == 'Sair' or event == sg.WIN_CLOSED:
        break




