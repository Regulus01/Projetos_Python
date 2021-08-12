import Funcoes

Vagas_Aviao = Funcoes.AmericanAirLines()  # avião
Cadastro_Cliente = {}  # cadastro dos clientes
reserva = {}   #reservas feitas
relatorio_cancel = []  #cancelamentos

try:
    Funcoes.carregar(Cadastro_Cliente)
except FileNotFoundError:
    open("cadastro.txt", "w")

try:
    Funcoes.carregar_reservas(reserva)
except FileNotFoundError:
    open("reservas.txt", "w")

try:
    Funcoes.loading(Vagas_Aviao, reserva)
except IndexError:
    pass

while True:
    opc = 0
    try:
        opc = int(input('\n\033[0;33m        ✈️Senhores passageiros sejam bem vindos, a AmericanAirLines ✈️'
                        '\033[0;00m '
                        '\n\nPor Favor, selecione uma opção em nosso console 👩'
                        '\n\n\033[0;32m1 - Cadastro de cliente \n2 - Consulta de clientes cadastrados por CPF'
                        '\n3 - Reserva de Assento \n4 - Cancelar reservas  \n5 - Assentos livres'
                        '\n6 - Relatório de Assentos cancelados \n7 - Relatório de reservas '
                        '\n0 - Desligar console\n\n\033[0;00mEscolha um número do menu:\033[0;00m '))
    except ValueError:
        print()
    if opc not in (0, 1, 2, 3, 4, 5, 6, 7):
        print('\nPor favor selecione somente as opções listadas')
    if opc == 0:
        print('\nObrigado por escolher a AmericanAirLines, tenha um ótimo vôo 🛫')
        print(f'\n{Funcoes.Aviao()}')
        break
    if opc == 1:
        print('\nMenu de cadastro do cliente para voltar ao menu inicial, digite 0')
        Funcoes.Cadastro_Clientes(Cadastro_Cliente)
    if opc == 2:
        print('\nMenu de consulta de clientes cadastrados para voltar ao menu digite 0')
        Funcoes.Consulta_Clientes(Cadastro_Cliente)
    if opc == 3:
        print('\nMenu de reserva de assento')
        Funcoes.Reserva_Assento(Vagas_Aviao, Cadastro_Cliente, reserva)
    if opc == 4:
        print('\nMenu de Cancelamento de Reserva')
        Funcoes.Cancelar_Reserva(Vagas_Aviao, Cadastro_Cliente, reserva, relatorio_cancel)
    if opc == 5:
        print('\nMenu de consulta de vagas livres')
        Funcoes.Vagas_Livres(Vagas_Aviao)
    if opc == 6:
        print('\nRelatório de cancelamentos')
        Funcoes.Cancelamentos()
    if opc == 7:
        print('\nMenu de Vagas Reservadas')
        Funcoes.Vagas_Reservadas(Vagas_Aviao)
