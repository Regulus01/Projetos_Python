import string

""" Alunos: José Cláudio, Kaio Ântonio Andrade Rodrigues, Luan De Carvalho Lima, Rodney Assis Furtado - Pycharm"""


def AmericanAirLines():
    vagas = []
    for x in range(20):
        linhas = []
        for i in range(4):
            linhas.append('💺')
        vagas.append(linhas)
    return vagas


def loading(vagas_aviao, reserva):
    contador = 0
    contador2 = 0
    teste = []
    teste += reserva.values()
    while True:
        vagas_aviao[teste[contador2][0]][teste[contador2][1]] = '👨'
        contador2 += 1
        contador += 1
        if contador == len(teste):
            break


def carregar(cliente_c):
    with open('cadastro.txt') as doc:
        for line in doc:
            (cpf, name) = line.split()
            cliente_c[cpf] = name


def carregar_reservas(reserva):
    with open('reservas.txt') as doc:
        for line in doc:
            (cpf, name, name2) = line.split()
            reserva[cpf] = [int(name), int(name2)]


def Cadastro_Clientes(cliente_c):
    while True:
        print('\nPara sair, digite 0')
        nome = input('\nDigite o seu nome: ').capitalize()
        if nome == '0':
            break
        while True:
            alphabetU = (list(string.ascii_uppercase))
            alphabetL = (list(string.ascii_lowercase))
            try:
                cpf = str(input('\nDigite os 11 números do seu CPF: '))
                if int(cpf) == alphabetU or int(cpf) == alphabetL:
                    print('')
                if cpf == '0':
                    break
                if len(str(cpf)) == 11 and cpf not in cliente_c.keys():
                    cliente_c[cpf] = nome
                    with open('cadastro.txt', 'a') as doc:
                        doc.write(str(cpf))
                        doc.write(str(' '))
                        doc.write(str(nome))
                        doc.write(str('\n'))
                    print('Cliente cadastrado com sucesso')
                    break
                if cpf in cliente_c.keys():
                    print('O CPF já consta em nosso banco de dados, tente novamente')
                if len(str(cpf)) != 11:
                    print('\n\033[0;31mDigite somente os 11 números do seu Cpf\033[0;00m')
            except ValueError:
                print('\n\033[0;31mDigite somente números\033[0;00m')
        sair = input('Deseja sair? S/N: ').upper()
        if sair == 'S':
            break


def Consulta_Clientes(client_c):
    while True:
        consulta_CPF = ''
        try:
            consulta_CPF = str(input('\nDigite seu CPF: '))
        except ValueError:
            print('\033[0;31mDigite somente Números\033[0;0m')
        if consulta_CPF == '0':
            break
        if consulta_CPF in client_c.keys():
            print(f'\n\033[0;33mO cliente {client_c[consulta_CPF]} está cadastrado\033[0;00m')
        else:
            print(f'\n\033[0;31mO número de CPF informado não está cadastrado\033[0;0m'
                  f'\n\033[0;34mVolte para o menu digitando 0 e cadastre o cliente\033[0;0m')


def Vagas_Livres(vagas):
    cont = 0
    while True:
        consulte = input('\nDeseja consultar as cadeiras livres? [S/N]\n').upper()
        if consulte == 'S':
            for k in range(0, 20):
                for i in range(0, 4):
                    if '💺' in vagas[k][i]:
                        cont += 1
            print(f'\n\033[0;33mTemos {cont} assentos livres no avião\033[0;00m')
            cont = 0
            print('        0      1      2     3')
            for k in range(0, len(vagas)):
                print(f'{k}       {" -=- ".join(vagas[k])}')
        else:
            break


def Aviao():
    return('\033[1;34m   ⣖⠲⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⢸⠉⡇'
    '\n⠀⠀⠀⠸⡆⠹⡀⣠⢤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⡏⠀⡧⢤⡄'
    '\n⠀⠀⠀⠀⡧⢄⣹⣅⣜⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀  ⢸⠁⠀⢹⠚⠃⠀'
    '\n⠀⣀⠴⢒⣉⡹⣶⣤⣀⡉⠉⠒⠒⠒⠤⠤⣀⣀⣀⠇⠀⠀⢸⠠⣄'
    '\n⠀⠈⠉⠁⠀⠀⠀⠉⠒⠯⣟⣲⠦⣤⣀⡀⠀⠀⠈⠉⠉⠉⠛⠒⠻⢥⣀⠀⠀⠀'
      '\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣲⡬⠭⠿⢷⣦⣤⢄⣀⠀⠀⠚⠛⠛⠓⢦⡀'
      '\n⠀⠀⠀⠀⠀⠀⠀⢀⣀⠤⠴⠚⠉⠁⠀⠀⠀⠀⣀⣉⡽⣕⣯⡉⠉⠉⠑⢒⣒⡾'
      '\n⠀⠀⣀⡠⠴⠒⠉⠉⠀⢀⣀⣀⠤⡤⢶⣶⣋⠉⠉⠀⠀⠀⠈⠉⠉⠉⠉⠉⠁⠀'
      '\n⣖⣉⣁⣠⠤⠶⡶⡶⢍⡉⠀⠀⠀⠙⠒⠯⠜⠀⠀⠀'
      '\n⠀⠁⠀⠀⠀⠀⠑⢦⣯⠇')


def Reserva_Assento(vagas_aviao, cadastro_cliente, reserva):
    while True:
        reserve = input('\nDeseja Reservar um assento? [S/N]: ').upper()
        if reserve == 'S':
            print('        0      1      2     3')
            for k in range(0, len(vagas_aviao)):
                print(f'{k}       {" -=- ".join(vagas_aviao[k])}')
            cpf = str(input('Digite seu CPF: '))
            if cpf in reserva.keys():
                print('\nJá consta uma reserva com esse CPF no nosso sistema, utilize outro cpf')
            elif cpf in cadastro_cliente.keys():
                fileira = 0
                try:
                    fileira = int(input('\nDigite a fileira que deseja reservar 0 a 19: '))
                    while fileira > 19 or fileira < -1:
                        print('Fileira invalida, tente novamente. Utilize números de 0 a 19')
                        fileira = int(input('\nDigite a fileira que deseja reservar 0 a 19: '))
                except ValueError:
                    print('\nDigite somente números')
                cadeira = 0
                try:
                    cadeira = int(input('Digite a coluna da cadeira que deseja reservar 0 a 3: '))
                    while cadeira > 3 or cadeira < -1:
                        print('Cadeira invalida, tente novamente. Utilize os números de 0 a 3')
                        cadeira = int(input('Digite a coluna da cadeira que deseja reservar 0 a 3: '))
                except ValueError:
                    print('\nDigite somente números')
                if vagas_aviao[fileira][cadeira] == '👨':
                    print('\nA cadeira se encontra reservada, tente novamente')
                else:
                    vagas_aviao[fileira][cadeira] = '👨'
                    reserva[cpf] = [fileira, cadeira]
                    with open('reservas.txt', 'a') as doc:
                        doc.write(str(cpf))
                        doc.write(str(' '))
                        doc.write(str(fileira))
                        doc.write(' ')
                        doc.write(str(cadeira))
                        doc.write(str('\n'))
                    print('Vaga reservada')
                    print('        0      1      2     3')
                    for k in range(0, len(vagas_aviao)):
                        print(f'{k}       {" -=- ".join(vagas_aviao[k])}')
            if cpf not in cadastro_cliente.keys():
                print('O cliente não está cadastrado')
        else:
            break


def Vagas_Reservadas(vagas_aviao):
    contador = 0
    for x in range(0, len(vagas_aviao)):
        print(f'Fileira {x}: {vagas_aviao[x].count("👨")} Reservada')
        if "👨" in vagas_aviao[x]:
            contador += 1
    print(f'Total de vagas reservadas: {contador}')


def Cancelamentos():
    while True:
        consulta = input('\nDeseja consultar o relatório de cancelamentos? [S/N] ').upper()
        if consulta == 'S':
            print('\n\033[0;31mCancelamentos registrados de acordo com CPF\033[0;00m\n')
            try:
                with open('relatorio_cancel.txt', 'r') as canc:
                    for linha in canc:
                        linha = linha.strip()
                        print(linha)
            except FileNotFoundError:
                open('relatorio_cancel.txt', 'w')


        else:
            break


def Cancelar_Reserva(vagas_aviao, cadastro_cliente, reserva, relatorio_cancel):
    while True:
        cancelamento = input('\nDeseja cancelar a sua reserva? [S/N] ').upper()
        if cancelamento == 'S':
            print('        0      1      2     3')
            for k in range(0, len(vagas_aviao)):
                print(f'{k}       {" -=- ".join(vagas_aviao[k])}')
            cpf_reserva = input('Digite seu CPF: ')
            if cpf_reserva in cadastro_cliente.keys() and cpf_reserva not in reserva.keys():
                print('\nO cpf cadastrado não efetuou nenhuma reserva')
                cpf_reserva = input('\nDigite seu CPF: ')
            if cpf_reserva in cadastro_cliente.keys() and cpf_reserva in reserva.keys():
                file = 0
                try:
                    file = int(input('\nDigite a fileira que deseja cancelar 0 a 19: '))
                    while file > 19 or file < -1:
                        print('Fileira invalida, tente novamente. Utilize números de 0 a 19')
                        file = int(input('\nDigite a fileira que deseja cancelar 0 a 19: '))
                except ValueError:
                    print('\nDigite somente números')
                cade = 0
                try:
                    cade = int(input('Digite a coluna da cadeira que deseja cancelar 0 a 3: '))
                    while cade > 3 or cade < -1:
                        print('Cadeira invalida, tente novamente. Utilize os números de 0 a 3')
                        cade = int(input('Digite a coluna da cadeira que deseja cancelar 0 a 3: '))
                except ValueError:
                    print('\nDigite somente números')
                if reserva[cpf_reserva] == [file, cade]:
                    print('\nCancelamento de reserva concluido com sucesso')
                    del reserva[cpf_reserva]
                    save_temp = list(reserva.keys())
                    save_temp2 = list(reserva.values())
                    with open('reservas.txt', 'w') as doc:
                        for k in range(0, len(reserva)):
                            doc.write(f'{str(save_temp[k])} {str(save_temp2[k][0])} {str(save_temp2[k][1])}\n')
                    vagas_aviao[file][cade] = '💺'
                    relatorio_cancel += cpf_reserva
                    with open('relatorio_cancel.txt', 'a') as canc:
                        canc.write(f'{cpf_reserva} Fileira: {file} Coluna: {cade}\n')
                    print('        0      1      2     3')
                    for k in range(0, len(vagas_aviao)):
                        print(f'{k}       {" -=- ".join(vagas_aviao[k])}')
                else:
                    print(f'A cadeira fileira {file} coluna {cade} não foi reservada pelo cliente {cpf_reserva}'
                          f'\nTente novamente')
            elif cpf_reserva not in cadastro_cliente.keys():
                print('\nO cliente não está cadastrado!')
                break
        else:
            break
