import pandas as pd


def Cadastro_Professor_Aluno(dados_professores, Matricula_professor, Nome_professor, data_pro,
                             arquivo):
    # função para cadastrar tanto professor quanto alunos
    dados_professores['Matricula'] += [Matricula_professor]
    dados_professores['Nome'] += [Nome_professor]
    dados_professores['Data de nascimento'] += [data_pro]
    excel = pd.DataFrame(data=dados_professores)
    with pd.ExcelWriter(arquivo) as writer:
        excel.to_excel(writer, index=False)


def Carregamento_Excel(arquivo_excel, index_coluna):
    # Função para carregar o arquivo excel em um dicionário parâmetros nome do arquivo e primeira coluna
    df = pd.read_excel(arquivo_excel)
    df.set_index(index_coluna).T.to_dict('list')
    return df.to_dict(orient='list')


def Cadastro_Notas(Notas, Codigo, Nome_Disciplina_Notas, Nome_Professor_nota, Matricula_Aluno_Notas, Nota_1 , Nota_2):
    # Função para cadastrar notas dos alunos
    Notas['Cod_disci'] += [Codigo]
    Notas['Disciplina'] += [Nome_Disciplina_Notas]
    Notas['Aluno'] += [Matricula_Aluno_Notas]
    Notas['Professor'] += [Nome_Professor_nota]
    Notas['Nota 1'] += [Nota_1]
    Notas['Nota 2'] += [Nota_2]
    Notas['Nota Final'] += [(Nota_1 + Nota_2)/2]
    excel = pd.DataFrame(data=Notas)
    with pd.ExcelWriter('Notas_Alunos.xlsx') as writer:
        excel.to_excel(writer, index=False)


def Cadastro_Disciplina(dados_disciplina, Codigo_Disciplina, Nome_Disciplina, Matricula_prof_Disciplina):
    dados_disciplina['Codigo_Disciplina'] += [Codigo_Disciplina]
    dados_disciplina['Nome_Disciplina'] += [Nome_Disciplina]
    dados_disciplina['Matricula_Professor_Disciplina'] += [Matricula_prof_Disciplina]
    excel = pd.DataFrame(data=dados_disciplina)
    with pd.ExcelWriter('Disciplina_Cadastradas.xlsx') as writer:
        excel.to_excel(writer, index=False)


def unit():
   return('\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
'\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⢀⠄⣤⣤⡀\033[0;00m⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄'
'\n⠄⠄⠄\033[0;34m⢀⣀⣀⣀\033[0;00m⠄\033[0;34m⢀⣀⣀⣀⣀⡀\033[0;00m⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⣷⠛⢿⣿⡙\033[0;00m⠂⠄⠄'
          '\033[0;34m⣀⣀⣀⡀\033[0;00m⠄⠄⠄'
'\n⠄⠄\033[0;34m⢰⣿⣿⣿⣿\033[0;00m⠄\033[0;34m⢸⣿⣿⣿⣿⡇\033[0;00m⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄\033[0;33m⠹⢶⣿⣿⠗\033[0;00m⠁⠄\033[0;34m'
          '⣾⣿⣿⣿⡇\033[0;00m⠄⠄⠄'
'\n⠄⠄\033[0;34m⢸⣿⣿⣿⣿\033[0;00m⠄\033[0;34m⢸⣿⣿⣿⣿⡇⢠⣶⣶⣶⣆⣴⣶⣿⣶⣦\033[0;00m⠄\033[0;34m⢰⣶⣶⣶⣶\033[0;00m⠄\033[0;34m'
          '⣶⣿⣿⣿⣿⣷⡆\033[0;00m⠄⠄'
'\n⠄⠄\033[0;34m⢸⣿⣿⣿⣿\033[0;00m⠄\033[0;34m⢸⣿⣿⣿⣿⡇⢸⣿⣿⣿⡿⠿⣿⣿⣿⣿⡇⢸⣿⣿⣿⣿\033[0;00m⠄\033[0;34m⠿⣿⣿⣿⣿⡿⠇\033[0;00m⠄⠄'
'\n⠄⠄\033[0;34m⠸⣿⣿⣿⣿⣄⣸⣿⣿⣿⣿⡇⢸⣿⣿⣿⡇\033[0;34m\033[0;00m⠄\033[0;34m⢸⣿⣿⣿⡇⢸⣿⣿⣿⣿\033[0;00m⠄⠄\033[0;34m⣿⣿⣿⣿⡇'
          '\033[0;00m⠄⠄⠄'
'\n⠄⠄⠄\033[0;34m⠻⣿⣿⣿⣿⣿⣿⣿⣿⠟\033[0;00m⠄\033[0;34m⢸⣿⣿⣿⡇\033[0;00m⠄\033[0;34m⢸⣿⣿⣿⡇⢸⣿⣿⣿⡿\033[0;00m⠄⠄'
          '\033[0;34m⣿⣿⣿⣿⡇\033[0;00m⠄⠄⠄'
'\n⠄⠄⠄⠄⠄\033[0;34m⠉⠛⠛⠛⠛⠋⠁\033[0;00m⠄⠄\033[0;34m⠘⠛⠛⠛⠃\033[0;00m⠄\033[0;34m⠘⠛⠛⠛⠃⠘⠛⠛⠛⠁'
          '\033[0;00m⠄⠄\033[0;34m⠛⠛⠛⠛⠃\033[0;00m⠄⠄⠄'
'\n⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄')