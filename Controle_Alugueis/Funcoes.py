import pandas as pd


class proprietario:
    # Classe para cadastro de proprietarios
    def __init__(self, Nome_Prop, CPF, data_nascimento):
        self.Nome_Prop = Nome_Prop
        self.CPF = CPF
        self.data_nascimento = data_nascimento

    def Armazenar_Nome(self):
        return self.Nome_Prop

    def Armazenar_CPF(self):
        return self.CPF

    def Armazenar_Data(self):
        return self.data_nascimento


class Imovel:
    # Classe para cadastro de imoveis
    def __init__(self, Codigo_Imovel, Cpf_Propr, Tipo, Endereco,
                 Valor_Aluguel, Status, Data_inicio, Data_fim):
        self.Codigo_Imovel = Codigo_Imovel
        self.Cpf_Propr = Cpf_Propr
        self.Tipo = Tipo
        self.Endereco = Endereco
        self.Valor_Aluguel = Valor_Aluguel
        self.Status = Status
        self.Data_inicio = Data_inicio
        self.Data_fim = Data_fim

    def Armazenar_Codigo(self):
        return self.Codigo_Imovel

    def Armazenar_Cpf_Propr(self):
        return self.Cpf_Propr

    def Armazenar_Tipo(self):
        return self.Tipo

    def Armazenar_Endereco(self):
        return self.Endereco

    def Armazenar_Aluguel(self):
        return self.Valor_Aluguel

    def Armazenar_Status(self):
        return self.Status

    def Armazenar_data_i(self):
        return self.Data_inicio

    def Armazenar_data_f(self):
        return self.Data_fim


class Inquilino:
    # Classe para cadastro de proprietarios
    def __init__(self, Nome_Inquilino, CPF, data_nascimento):
        self.Nome_Inquilino = Nome_Inquilino
        self.CPF = CPF
        self.data_nascimento = data_nascimento

    def Armazenar_Nome(self):
        return self.Nome_Inquilino

    def Armazenar_CPF(self):
        return self.CPF

    def Armazenar_Data(self):
        return self.data_nascimento


def Cadastro(Cadastro_Proprietario, dados, arquivo):
    # função para cadastrar os proprietarios no dicionario e excel

    Cadastro_Proprietario['Nome'] += [dados.Armazenar_Nome()]
    Cadastro_Proprietario['CPF'] += [dados.Armazenar_CPF()]
    Cadastro_Proprietario['Data_Nascimento'] += [dados.Armazenar_Data()]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def Cadastro_imovel(Cadastro_Proprietario, dados, arquivo):
    # função para cadastrar os imoveis no dicionario e excel

    Cadastro_Proprietario['Codigo'] += [dados.Armazenar_Codigo()]
    Cadastro_Proprietario['CPF_PROP'] += [dados.Armazenar_Cpf_Propr()]
    Cadastro_Proprietario['Tipo'] += [dados.Armazenar_Tipo()]
    Cadastro_Proprietario['Endereço'] += [dados.Armazenar_Endereco()]
    Cadastro_Proprietario['Valor_Aluguel'] += [dados.Armazenar_Aluguel()]
    Cadastro_Proprietario['Status'] += [dados.Armazenar_Status()]
    Cadastro_Proprietario['Data_inicio'] += [dados.Armazenar_data_i()]
    Cadastro_Proprietario['Data_f'] += [0]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def Cadastro_aluguel(Cadastro_Proprietario, dados, arquivo):
    # função para cadastrar os alugueis no dicionario e excel

    Cadastro_Proprietario['Codigo'] += [dados.Armazenar_Codigo()]
    Cadastro_Proprietario['CPF_INQ'] += [dados.Armazenar_Cpf_Propr()]
    Cadastro_Proprietario['Tipo'] += [dados.Armazenar_Tipo()]
    Cadastro_Proprietario['Endereço'] += [dados.Armazenar_Endereco()]
    Cadastro_Proprietario['Aluguel'] += [dados.Armazenar_Aluguel()]
    Cadastro_Proprietario['Status'] += [dados.Armazenar_Status()]
    Cadastro_Proprietario['Data_i'] += [0]
    Cadastro_Proprietario['Data_f'] += [0]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def Arrecada_imoveis(Cadastro_Proprietario, codigo, arrecada, arquivo):
    # função para cadastrar os imoveis no dicionario e excel

    Cadastro_Proprietario['Codigo'] += [codigo]
    Cadastro_Proprietario['Arrecadacao'] += [arrecada]
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def w_excel(Cadastro_Proprietario, arquivo):
    excel = pd.DataFrame(data=Cadastro_Proprietario)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def cp_2077():
    print('\033[1;33m ⠄⢠⣄⣄⣄⣤⣀⣄⠄⠄⠄⠄⠄⠄⠄⣠⣄⣤⣠⣄⠄⠄⠄⠄⠄⠄⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿'
          '\n⢀⣶⣿⣿⠟⠿⠿⣿⣿⣿⠆⠄⠄⠄⣰⣷⠿⠛⠛⠹⣻⣶⣆⠄⠄⠄⠰⠿⠿⠿⠿⠿⠿⣿⣿⣿⠃⠄⠄⠰⠿⠿⠿⠿⠿⠿⣿⣿⡿⠃'
          '\n⠘⠛⠛⠻⠄⠄⢀⣾⣿⣿⠇⠄⠄⢰⣿⢿⠁⠄⠄⠄⠈⣿⣷⡄⠄⠄⠄⠄⠄⠄⠄⢀⣼⣿⣿⠃⠄⠄⠄⠄⠄⠄⠄⠄⠄⣾⣿⣿⠃⠄'
          '\n⠄⠄⠄⠄⣀⣠⣿⣿⣿⠏⠁⠄⠄⢸⣿⡏⠄⠄⠄⠄⠄⢻⣿⠁⠄⠄⠄⠄⠄⠄⣠⣾⣿⣿⠁⠄⠄⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⠇⠄⠄'
          '\n⠄⠄⢴⣴⣿⣿⡟⠉⠁⠄⠄⠄⠄⢘⣿⣽⠄⠄⠄⠄⠄⣿⣿⡄⠄⠄⠄⠄⠄⢠⣾⣿⣿⡏⠄⠄⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⠇⠄⠄⠄'
          '\n⢀⣶⣿⣿⣿⣿⣶⣶⣶⣶⣶⠄⠄⠈⠿⣷⣦⣀⣀⣀⣴⣿⡿⠁⠄⠄⠄⠄⠄⣸⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⣿⡇⠄⠄⠄'
          '\n⠜⠛⠛⠛⠛⠛⠛⠛⠛⠛⠻⠄⠄⠄⠈⠘⠿⠿⠿⠿⠿⠋⠁⠄⠄⠄⠄⠄⠄⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠿⠿⠿⠿⠇⠄⠄⠄')
