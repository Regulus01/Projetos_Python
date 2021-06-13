import Funcoes
import FuncoesEmpresa
import pandas as pd
import string


Cadastro_Proprietario = {'Nome': [], 'CPF': [], 'Data_Nascimento': []}
try:
    Cadastro_Proprietario = FuncoesEmpresa.Carregamento_Excel('Proprietarios.xlsx', 'Nome')
except FileNotFoundError:
    pass

Imoveis_Cadastrados = {'Codigo': [], 'CPF_PROP': [], 'Tipo': [], 'Endereço': [], 'Valor_Aluguel': [],
                       'Status': [], 'Data_inicio': [], 'Data_f': []}
try:
    Imoveis_Cadastrados = FuncoesEmpresa.Carregamento_Excel('Imoveis_Cadastrados.xlsx', 'Codigo')
except FileNotFoundError:
    pass

Cadastro_Inquilino = {'Nome': [], 'CPF': [], 'Data_Nascimento': []}
try:
    Cadastro_Inquilino = FuncoesEmpresa.Carregamento_Excel('Inquilinos.xlsx', 'Nome')
except FileNotFoundError:
    pass

Alugueis_Registrados = {'Codigo': [], 'CPF_INQ': [], 'Tipo': [], 'Endereço': [], 'Aluguel': [],
                        'Status': [], 'Data_i': [], 'Data_f': []}
try:
    Alugueis_Registrados = FuncoesEmpresa.Carregamento_Excel('Alugueis_Registrados.xlsx', 'Codigo')
except FileNotFoundError:
    pass

Comissoes = {'Codigo': [], 'Arrecadacao': []}

try:
    Comissoes = FuncoesEmpresa.Carregamento_Excel('Arrecadacao.xlsx', 'Codigo')
except FileNotFoundError:
    pass

# lista que armazenam valores dos dicionarios
comi_temp = list(Comissoes.values())
CPF_TEMP = list(Cadastro_Proprietario.values())
Imoveis_Temp = list(Imoveis_Cadastrados.values())
CPF_INQUI = list(Cadastro_Inquilino.values())

Funcoes.cp_2077()
print('\n\033[1;95mBem vindo a CyberCorretora sua corretora do futuro')
print('\nAcorde Samurai, nos temos imoveis para alugar')
while True:
    Menu = str(input('\n \033[1;94m1 - Cadastrar Proprietario'  # 100%
                     '\n 2 - Cadastrar Imóvel'  # 100%
                     '\n 3 - Cadastrar Inquilino'  # 90%
                     '\n 4 - Registrar Aluguel'  # 90% - Programa - linha 177 e 179 sem cor
                     '\n 5 - Finalizar Aluguel'  # 90%
                     '\n 6 - Relatório de Proprietários'  # 100% - falta cor
                     '\n 7 - Relatório de Imóveis'  # 100% - falta cor
                     '\n 8 - Relatório de Inquilinos'  # 100% - falta cor
                     '\n 9 - Relatório de Aluguéis'  # 100% - falta cor
                     '\n10 - Relatório de Comissões'  # 100% - falta cor,
                     '\n 0- Sair'
                     '\n\n\033[1;96m O que deseja?:\033[0;00m '))

    if Menu == '1':  # Cadastrar proprietário
        while True:
            Alphabet = list(string.ascii_letters) + list(string.punctuation)
            Nome = input('\nDigite o seu nome: ').title()
            CPF = ''
            while type(CPF) == str:
                CPF = FuncoesEmpresa.Tratamento_Cpf(CPF_TEMP)
            while True:
                try:
                    Nasc_prop = input('\nDigite sua data de nascimento Ex: 16051998: ')
                    data = FuncoesEmpresa.Cadastro_Data(Nasc_prop)
                except ValueError or OverflowError:
                    print('\n\033[0;31mData digitada no formato errado ou contem letras,'
                          ' digite novamente!\033[0;00m ')
                else:
                    break
            dados = Funcoes.proprietario(Nome, CPF, data)
            Funcoes.Cadastro(Cadastro_Proprietario, dados, 'Proprietarios.xlsx')
            print('\n\033[0;32mUsuário cadastrado com sucesso!\033[0;32m')
            break

    if Menu == '2':  # Cadastrar Imóvel
        Codigo_Imovel = ''
        while type(Codigo_Imovel) != int or Codigo_Imovel in Imoveis_Temp[0]:
            try:
                Codigo_Imovel = int(input('\nDigite o código do imóvel: '))
            except ValueError:
                print('\n\033[0;31mO código do imovel deve possuir apenas números!\033[0;00m')
            if Codigo_Imovel in Imoveis_Temp[0]:
                print('\n\033[0;31mO imóvel se encontra cadastrado no sistema\033[0;00m')

        Cpf_Propr = FuncoesEmpresa.Tratamento_Cpf_Imovel(CPF_TEMP)
        Tipo = ''
        while Tipo not in ['CASA', 'APARTAMENTO']:
            Tipo = input('\nDigite o tipo do imóvel [CASA/APARTAMENTO]: ').upper()
            if Tipo not in ['CASA', 'APARTAMENTO']:
                print('\n\033[0;31mDigite somente Casa ou Apartamento\033[0;00m')

        Endereco = input('Digite o seu endereço: ')
        Valor_Aluguel = 0
        while True:
            try:
                Valor_Aluguel = float(input('Digite o valor do aluguel: '))
            except ValueError or OverflowError:
                print('\n\033[0;31mDigite somente números no Aluguel\n\033[0;00m')
            else:
                break
        Status = ''
        while Status not in ['S', 'N']:
            Status = input('O apartamento está alugado [S/N]: ').upper()
            if Status not in ['S', 'N']:
                print('\n\033[0;31mDigite somente S ou N\033[0;00m')
        data_inicio = 0
        data_fim = 0
        dados_imovel = Funcoes.Imovel(Codigo_Imovel, Cpf_Propr, Tipo, Endereco, Valor_Aluguel,
                                      Status, data_inicio, data_fim)
        Funcoes.Cadastro_imovel(Imoveis_Cadastrados, dados_imovel, 'Imoveis_Cadastrados.xlsx')
        print('\n\033[0;32mImóvel cadastrado com sucesso!\033[0;32m')

    if Menu == '3':  # Cadastrar Inquilino
        Nome = input('\nDigite o seu nome: ').title()
        CPF = FuncoesEmpresa.Tratamento_Cpf(CPF_INQUI)
        while True:
            try:
                Nasc_Inquilino = input('\nDigite sua data de nascimento Ex: 16051998: ')
                data = FuncoesEmpresa.Cadastro_Data(Nasc_Inquilino)
            except ValueError or OverflowError:
                print('\n\033[0;31mData digitada no formato errado ou contem letras'
                      ', digite novamente!\033[0;00m ')
            else:
                break
        dados = Funcoes.Inquilino(Nome, CPF, data)
        Funcoes.Cadastro(Cadastro_Inquilino, dados, 'Inquilinos.xlsx')
        print('\n\033[0;32mUsuário cadastrado com sucesso!\033[0;32m')

    if Menu == '4':  # Registrar Aluguel
        data_fim = '---'
        print('\nMenu para finalizar alugueis, para sair digite -1 no cpf')
        while True:
            cpf_inquilino = int(input('Digite o cpf do inquilino: '))
            codigo_imo = int(input('Digite o código do imóvel: '))
            if cpf_inquilino in CPF_INQUI[1] and codigo_imo in Imoveis_Temp[0]:
                local = Imoveis_Cadastrados['Codigo'].index(codigo_imo)
                if Imoveis_Cadastrados['Status'][local] == 'N':
                    while True:
                        try:
                            data_inicio = input('Digite a data de inicio do aluguel: ')
                            data_i = FuncoesEmpresa.Cadastro_Data(data_inicio)
                            print(data_i)
                        except ValueError:
                            print('\n\033[0;31mData digitada no formato errado '
                                  'ou contem letras, digite novamente!\033[0;00m ')
                        else:
                            break

                    # local = Imoveis_Cadastrados['Codigo'].index(codigo_imo)
                    Imoveis_Cadastrados['Status'][local] = 'S'
                    Imoveis_Cadastrados['Data_inicio'][local] = data_i
                    Funcoes.w_excel(Imoveis_Cadastrados, 'Imoveis_Cadastrados.xlsx')
                    print('\nAluguel Realizado com sucesso! ')
                    # apos será registrado o aluguel para o relatorio, op 9
                    imovel_Aluguel = Funcoes.Imovel(codigo_imo, cpf_inquilino, Imoveis_Cadastrados['Tipo'][local],
                                                    Imoveis_Cadastrados['Endereço'][local],
                                                    Imoveis_Cadastrados['Valor_Aluguel'][local],
                                                    Imoveis_Cadastrados['Status'][local], data_i, data_fim)

                    Funcoes.Cadastro_aluguel(Alugueis_Registrados, imovel_Aluguel, 'Alugueis_Registrados.xlsx')
                    # registro de arrecadação do aluguel a cada aluguel será adicionado o valor do mês aluguel
                    if codigo_imo not in comi_temp[0]:
                        Funcoes.Arrecada_imoveis(Comissoes, codigo_imo, Imoveis_Cadastrados['Valor_Aluguel'][local],
                                                 'Arrecadacao.xlsx')
                    else:
                        local_x = Comissoes['Codigo'].index(codigo_imo)
                        Comissoes['Arrecadacao'][local_x] += Imoveis_Cadastrados['Valor_Aluguel'][local]
                        Funcoes.w_excel(Comissoes, 'Arrecadacao.xlsx')
                    break
                else:
                    print('\nO imóvel se encontra alugado.')
            else:
                print('\nO cpf do inquilino ou código do imovel não consta no sistema')
                break

    if Menu == '5':  # finalização de alugueis
        print('\nMenu para finalizar alugueis, para sair digite -1 no cpf')
        while True:
            cpf_inqui = int(input('\nDigite o CPF do inquilino: '))
            if cpf_inqui == -1:
                break
            codigo_imo = int(input('Digite o código do imóvel: '))
            if cpf_inqui in CPF_INQUI[1] and codigo_imo in Imoveis_Temp[0]:
                local_f = Imoveis_Cadastrados['Codigo'].index(codigo_imo)
                if cpf_inqui in CPF_INQUI[1] and codigo_imo in Imoveis_Temp[0] \
                        and Imoveis_Cadastrados['Status'][local_f] == 'S':
                    while True:
                        try:
                            data_final = input('Digite a data de finalização do aluguel: ').strip()
                            data = FuncoesEmpresa.Cadastro_Data(data_final)
                        except ValueError:
                            print('\n\033[0;31mData digitada no formato errado '
                                  'ou contem letras, digite novamente!\033[0;00m ')
                        else:
                            break
                    # local_f = Imoveis_Cadastrados['Codigo'].index(codigo_imo)
                    Imoveis_Cadastrados['Data_f'][local_f] = data_final
                    Imoveis_Cadastrados['Status'][local_f] = 'N'
                    Funcoes.w_excel(Imoveis_Cadastrados, 'Imoveis_Cadastrados.xlsx')
                    print('\nAluguel finalizado com sucesso!')
                    # Logo abaixo o aluguel que está ocorrendo será finalizado para o relatorio, op 9
                    local_f = Alugueis_Registrados['Codigo'].index(codigo_imo)
                    Alugueis_Registrados['Codigo'][local_f] = f'{codigo_imo}-F'
                    Alugueis_Registrados['Data_f'][local_f] = data_final
                    Alugueis_Registrados['Status'][local_f] = 'F'
                    Funcoes.w_excel(Alugueis_Registrados, 'Alugueis_Registrados.xlsx')

                else:
                    print('\n\033[0;31mO imóvel se encontra desalugado.\033[0;00m')
            else:
                print('\n\033[0;31mO cpf do inquilino ou código do imovel não consta no sistema\033[0;00m')
                break

    if Menu == '6':  # Relatorio de proprietarios
        print('\nRelatorio de proprietarios cadastrados\n')
        try:
            print(pd.read_excel('Proprietarios.xlsx'))
        except FileNotFoundError:
            print("\n\033[0;31mNão há proprietarios cadastradas\033[0;00m")
        input('\nDigite qualquer botao para sair: ')

    if Menu == '7':  # Relatorio de imoveis
        print('\nRelatorio de imoveis cadastrados\n')
        try:
            print(pd.read_excel('Imoveis_Cadastrados.xlsx'))
        except FileNotFoundError:
            print("\n\033[0;31mNão há imoveis cadastrados\033[0;00m")
        input('\nDigite qualquer botao para sair: ')

    if Menu == '8':
        print('\nRelatorio de Inquilinos cadastrados\n')
        try:
            print(pd.read_excel('Inquilinos.xlsx'))
        except FileNotFoundError:
            print("\n\033[0;31mNão há inquilinos cadastrados\033[0;00m")
        input('\nDigite qualquer botao para sair: ')

    if Menu == '9':
        print('\nRelatorio de Alugueis Registrados\n')
        try:
            print(pd.read_excel('Alugueis_Registrados.xlsx'))
        except FileNotFoundError:
            print("\n\033[0;31mNão há alugueis registrados cadastrados\033[0;00m")
        input('\nDigite qualquer botao para sair: ')

    if Menu == '10':
        print('\nRelatorio de Arrecadação\n')
        try:
            print(pd.read_excel('Arrecadacao.xlsx'))
        except FileNotFoundError:
            print("\n\033[0;31mNão há alugueis registrados cadastrados\033[0;00m")
        input('\nDigite qualquer botao para sair: ')

    if Menu == '0':
        break
