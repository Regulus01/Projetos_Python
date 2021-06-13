import datetime
import pandas as pd
import string


def Cadastro_Data(data):
    # Funcao para retornar a data
        data_f = datetime.date(int(data[4:]),
                               int(data[2:4]),
                               int(data[:2]))
        return data_f


def Tratamento_Cpf(CPF_TEMP):
    # Função utilizada para tratar e inserir o cpf
    Alphabet = list(string.ascii_letters) + list(string.punctuation)
    cpf = ''
    Letra = ''
    try:
        while len(str(cpf)) != 11 or int(cpf) in CPF_TEMP[1]:
            cpf = str(input(f'\nInforme seu CPF: '))
            for i in cpf:
                if i in Alphabet:
                    Letra = i
            if Letra in Alphabet:
                print('\n\033[0;31mInforme somente números no CPF!\033[0;00m')
            elif len(str(cpf)) != 11:
                print(f'\n\033[0;31mInforme somente os 11 números do CPF!\033[0;00m')
            elif Letra not in Alphabet:
                if int(cpf) in CPF_TEMP[1]:
                    print('\n\033[0;31mO cpf consta em nosso banco de dados, digite '
                          'novamente\033[0;00m')
            Letra = ''
        else:
            if Letra in Alphabet:
                return 'b'
            else:
                return int(cpf)
    except ValueError:
        return 'b'




def Tratamento_Cpf_Imovel(CPF_TEMP):
    # Funcao para tratar erros do CPF no cadastro de imovel
    print(CPF_TEMP)
    cpf = ''
    while len(str(cpf)) != 11 or int(cpf) not in CPF_TEMP:
        cpf = str(input(f'\nInforme seu CPF: '))
        print(int(cpf))
        if len(str(cpf)) != 11:
            print(f'\n\033[0;31mInforme somente os 11 números do CPF!\033[0;00m')
        elif int(cpf) in CPF_TEMP[1]:
            return int(cpf)
        elif int(cpf) or cpf not in CPF_TEMP[1]:
            print('\n\033[0;31mO cpf não consta em nosso banco de dados, digite novamente ou selecione'
                  ' o menu 1 e faça o cadastro de proprietário.\033[0;00m')


def Carregamento_Excel(arquivo_excel, index_coluna):
    # Função para carregar o arquivo excel em um dicionário parâmetros nome do arquivo e primeira coluna
    # (Arquivo Excel: 'Alunos_Cadastrados.xlsx', Nome da primeira coluna: 'Matricula')
    df = pd.read_excel(arquivo_excel)
    df.set_index(index_coluna).T.to_dict('list')
    return df.to_dict(orient='list')