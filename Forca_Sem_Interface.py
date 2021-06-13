from random import choice
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
Nome_Escolhido = []   #armazena o nome tema da forca
Acertos = []
Digitadas = []
ContaErros = 0
ContAcertos = []
print('Bem vindo a forca, voce poderá escolher entre 6 temas sendo um da sua escolha 🤾‍!')
while True:
    print('Se digitado Escolha, você poderá digitar a palavra chave da forca!')
    Tema = input('\nDigite o tema da forca: Nomes(Próprios), Frutas, '
                 'Carros, Aleatorio, Anime, Jogos ou Escolha:\n').capitalize()
    teste = ['Nomes', 'Frutas', 'Carros', 'Aleatorio', 'Anime', 'Jogos', 'Escolha']
    teste2 = [Nomes, Frutas, Carros, Aleatorio, Anime, Jogos]
    if Tema in teste:
        if Tema == 'Escolha':
            Nome_Escolhido += input('\nDigite um nome de sua preferencia:\n').upper()
            for x in range(200):
                print('')
        else:
            for k in range(0, 6):
                if Tema == teste[k-1]:
                    print(k)
                    Nome_Escolhido += choice(teste2[k])        #escolhe uma plavra no tema e recebe separada
        break
    else:
        print('\nEscolha somente os Temas listados')
Erros = 0
while True:
    try:
        Erros = int(input('Qual maximo de erros você deseja ter na forca 3 ou 6?\n'))
    except ValueError:
        print('Não temos essa quantidade digite novamente')
    if Erros in (3, 6):
        break
    else:
        print('Não temos essa quantidade digite novamente')

q = ''    #junta as letras separadas usando .join
x = ' , ' #virgula entre as letras digitadas usando .join
z = '-'*60
Acertos += Nome_Escolhido      #adiciona o nome escolhido na lista de acertos e separa as letras
for k in range(len(Acertos)):  #percorre a lista de acertos de acordo com a separação da palavra
    Acertos[k] = '❏'           #troca todas as letras por ''❏''
print(f'\n{z}Inicio do jogo{z}!')
print(f'Palavra: {q.join(Acertos)} \n{len(Acertos)} Letras')
print(' ____________'
      '\n/            |'
      '\n|          '
      '\n|           '        
      '\n|            '
      '\n|          '
      '\n|')
while True:
    Digitadas1 = input('\nDigite uma letra: ').upper()
    for i in range(len(Nome_Escolhido)):    #percorre a lista do nome escolhido e conta as letras
        if Digitadas1 == Nome_Escolhido[i]: #verifica se a lista 'Digitadas' tem letras do 'Nome_Escolhido'
            Acertos[i] = Digitadas1         #Acertos recebe se a letra estiver no nome escolhido e os ❏ são trocados
            if Digitadas1 not in ContAcertos:
                ContAcertos.append(Digitadas1)
    if Digitadas1 in Digitadas:
        print('\nLetra repetida!')
    elif Digitadas1 not in Nome_Escolhido:
        print('\nNão tem essa letra na palavra!')
        ContaErros += 1
    if ContaErros == 1 and Erros == 3:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|  '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 2 and Erros == 3:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|             '
              '\n|')
    if ContaErros == 3 and Erros == 3:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|        / \  '
              '\n|')
    if ContaErros == 1 and Erros == 6:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|          '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 2 and Erros == 6:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /  '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 3 and Erros == 6:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|  '
              '\n|            '
              '\n|           '
              '\n|')

    if ContaErros == 4 and Erros == 6:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|            '
              '\n|          '
              '\n|')
    if ContaErros == 5 and Erros == 6:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|          '
              '\n|')
    if ContaErros == 6 and Erros == 6:
        print(' __________'
              '\n/         |'
              '\n|         O'
              '\n|        /|\  '
              '\n|         |   '
              '\n|        / \  '
              '\n|')
    Digitadas += Digitadas1
    if Nome_Escolhido == Acertos:
        print(f'\nVocê ganhou!\n Palavra: {q.join(Nome_Escolhido)} ')
        break
    if ContaErros == Erros:
        print(f'\nVocê errou {ContaErros} vezes então perdeu o jogo \nA palavra era {q.join(Nome_Escolhido)}')
        break
    print(f'Letras usadas: {x.join(Digitadas)} '
          f'\nAcertos: {len(ContAcertos)} \nErros: {ContaErros} \n {q.join(Acertos)}')
