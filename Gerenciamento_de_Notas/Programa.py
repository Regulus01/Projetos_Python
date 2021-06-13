import datetime
import pandas as pd
import Funcoes_Prof_Aluno  # Mudar aqui

dados_professores = {'Matricula': [], 'Nome': [], 'Data de nascimento': []}
try:
    dados_professores = Funcoes_Prof_Aluno.Carregamento_Excel('Professores_Cadastrados.xlsx', 'Matricula')
except FileNotFoundError or KeyError:
    pass

dados_aluno = {'Matricula': [], 'Nome': [], 'Data de nascimento': []}
try:
    dados_aluno = Funcoes_Prof_Aluno.Carregamento_Excel('Alunos_Cadastrados.xlsx', 'Matricula')
except FileNotFoundError or KeyError:
    pass
Notas = {'Cod_disci': [], 'Disciplina': [], 'Professor': [],
         'Aluno': [], 'Nota 1': [], 'Nota 2': [], 'Nota Final': []}
try:
    Notas = Funcoes_Prof_Aluno.Carregamento_Excel('Notas_Alunos.xlsx', 'Cod_disci')
except FileNotFoundError or KeyError:
    pass
dados_disciplina = {'Codigo_Disciplina': [], 'Nome_Disciplina': [], 'Matricula_Professor_Disciplina': []}
try:
    dados_disciplina = Funcoes_Prof_Aluno.Carregamento_Excel('Disciplina_Cadastradas.xlsx', 'Codigo_Disciplina')
except FileNotFoundError or KeyError:
    pass
'''Essas lista armazenam os codigos de disciplinas ou matriculas, 
    para validação em determinadas
    partes do código'''

Matriculas_Professores = list(dados_professores.values())
Matricula_Alunos = list(dados_aluno.values())
Codigos_Disciplinas = list(dados_disciplina.values())

print('\033[1;33m\n  Unit, preparando para o mundo, todos os dias.\033[0;00m')
print(Funcoes_Prof_Aluno.unit())
print('    \n         \033[1;35mSeja bem vindo ao Novo Magister')
while True:
    Opcao = int(input("\033[0;32m\n[1] - Cadastrar professores\n"
                      "[2] - Cadastrar aluno\n"
                      "[3] - Cadastrar disciplina\n"
                      "[4] - Cadastrar Nota\n"
                      "[5] - Relatorio de notas\n"
                      "[0] - Desligar Sistema\n"
                      "\n\033[0;33mEscolha uma das alternativas:\033[0;00m "))
    #  Cadastro de Professores (Nome, matrícula, data de nascimento)
    if Opcao == 1:  # Cadastro dos professores
        while True:
            print('\n\033[0;32mPara sair digite 0 na matricula\033[0;00m')
            try:
                Matricula_professor = int(input("\nDigite o número de matricula: "))
                if Matricula_professor == 0:
                    break
                elif int(Matricula_professor) in Matriculas_Professores[0]:
                    print("\033[0;31mEste usuario encontrasse cadastrado no nosso banco de dados.\033[0;00m ")
                    break
            except ValueError:
                print('\033[0;31mA Matrícula Deve Possuir Apenas Números!\033[0;00m')
                break
            Nome_professor = input('Digite o nome do professor: ').title().strip()
            if any(k.isdigit() for k in Nome_professor):
                print('\033[0;31mFormato de Nome Inválido\033[0;00m')
                break
            print('\nDigite a data de nascimento no formato 16051998')
            Data_Professores = input('\nDigite a data de nascimento: ')
            try:
                data_pro = datetime.date(int(Data_Professores[4:]),
                                         int(Data_Professores[2:4]),
                                         int(Data_Professores[:2]))
            except ValueError:
                print('\033[0;31mFormato de data errado\033[0;00m')
                break

            print('\n\033[0;32mProfessor cadastrado com sucesso!\033[0;00m')
            Funcoes_Prof_Aluno.Cadastro_Professor_Aluno(dados_professores, Matricula_professor,
                                                        Nome_professor, data_pro,
                                                        'Professores_Cadastrados.xlsx')

    if Opcao == 2:  # Cadastro Aluno
        while True:
            print('\n\033[0;32mPara sair digite 0 na matricula\033[0;00m')
            try:
                Matricula_Aluno = int(input('\nDigite o número da matricula: '))
                if Matricula_Aluno == 0:
                    break
                elif int(Matricula_Aluno) in Matricula_Alunos[0]:
                    print("\033[0;31m\nEste usuario encontrasse cadastrado em nosso banco de dados\033[0;00m. ")
                    break
            except ValueError:
                print('\033[0;31mA Matrícula Deve Possuir Apenas Números!\033[0;00m')
                break
            Nome_aluno = input('Digite o nome do aluno: ')
            if any(k.isdigit() for k in Nome_aluno):
                print('\033[0;31mFormato de Nome Inválido!\033[0;00m')
                break
            Data_Aluno = input('Digite a data de nascimento: ')
            try:
                Data_A = datetime.date(int(Data_Aluno[4:]),
                                       int(Data_Aluno[2:4]),
                                       int(Data_Aluno[:2]))
            except ValueError:
                print('\033[0;31mFormato de data errado\033[0;00m')
                break
            Funcoes_Prof_Aluno.Cadastro_Professor_Aluno(dados_aluno, Matricula_Aluno, Nome_aluno, Data_A,
                                                        'Alunos_Cadastrados.xlsx')
            print('\n\033[0;32mAluno Cadastrado com sucesso!\033[0;00m')

    if Opcao == 3:  # Cadastro de disciplina
        while True:
            print('\n\033[0;32mPara sair digite 0 no Codigo\033[0;00m')
            try:
                Codigo_Disciplina = int(input('Digite o Código da disciplina: '))
                if Codigo_Disciplina == 0:
                    break
                elif Codigo_Disciplina in Codigos_Disciplinas[0]:
                    print('\033[0;31mEsta disciplina já consta em nosso banco de dados!\033[0;00m')
                    break
            except ValueError:
                print('\033[0;31mFormato de Código Inválido!\033[0;00m')
                break
            Nome_Disciplina = input('Digite o nome da disciplina: ').title()
            try:
                Matricula_prof_Disciplina = int(input('Digite o número de matricula do professor: '))
            except ValueError:
                print('\033[0;31mFormato de Matricula Inválido!\033[0;00m')
                break
            if Matricula_prof_Disciplina not in Matriculas_Professores[0]:
                print('\033[0;31mO professor não está cadastrado, cadastre o professor utilizando a opção [1]\033[0;00m')
                break
            Funcoes_Prof_Aluno.Cadastro_Disciplina(dados_disciplina, Codigo_Disciplina, Nome_Disciplina,
                                                   Matricula_prof_Disciplina)
            print('\033[0;32m\nDisciplina cadastrada com sucesso!\033[0;00m')

    if Opcao == 4:  # Cadastro de Notas
        while True:
            print('Para sair digite 0 no codigo')
            try:
                Codigo_Diciplina_Notas = int(input('\nDigite o código da disciplina: '))
                if Codigo_Diciplina_Notas == 0:
                    break
                if Codigo_Diciplina_Notas not in Codigos_Disciplinas[0]:
                    print('\033[0;31mEsta disciplina nao consta em nosso banco de dados!\033[0;00m')
                    break
            except ValueError:
                print('\033[0;31mFormato de Código Inválido!\033[0;00m')
                break
            Nome_Disciplina_Notas = input('\nNome da disciplina: ').title().strip()
            if Nome_Disciplina_Notas not in Codigos_Disciplinas[1]:
                print('\nDisciplina não esta cadastrada volte e escolha a opcao [3] do menu')
                break
            Nome_Professor_nota = input('Digite o nome do professor: ').title().strip()
            if Nome_Professor_nota not in Matriculas_Professores[1]:
                print('\nO nome do professor nao se encontra cadastrado')
                break
            Matricula_Aluno_Notas = input('Digite a Matricula do aluno: ')
            if int(Matricula_Aluno_Notas) not in Matricula_Alunos[0]:
                print('\nAluno nao cadastrado cadastre o aluno na opcao [2] do menu')
                break
            Nota_1 = int(input('Nota da primeira unidade: '))
            Nota_2 = int(input('Nota da segunda unidade: '))
            Funcoes_Prof_Aluno.Cadastro_Notas(Notas, Codigo_Diciplina_Notas, Nome_Disciplina_Notas,
                                              Nome_Professor_nota, Matricula_Aluno_Notas, Nota_1, Nota_2)
            print('\033[0;32m\nNotas inseridas com sucesso!\033[0;00m')
    #  Cadastro de Notas(Código da Disciplina, matrícula do aluno, Nota   1, Nota  2) (0, 4)

    if Opcao == 5:  # Leitura do relatorio de notas
        try:
            print(pd.read_excel('Notas_Alunos.xlsx'))
        except FileNotFoundError:
            print("\nNão há notas cadastradas")

    if Opcao == 0: #Desligar o progama
        break
