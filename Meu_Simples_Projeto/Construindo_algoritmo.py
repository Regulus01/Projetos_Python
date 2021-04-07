

lista = cadastramento.values()


lista = [[1, 'crm', 'cpf'], [2, 'crm', 'cpf'], [1, 'crm', 'cpf'], [3, 'crm', 'cpf'],
         [1, 'crm', 'cpf'], [2, 'crm', 'cpf'], [1, 'crm', 'cpf'], [3, 'crm', 'cpf'],
         [1, 'crm', 'cpf'], [2, 'crm', 'cpf'], [1, 'crm', 'cpf'], [3, 'crm', 'cpf'],
         [1, 'crm', 'cpf'], [2, 'crm', 'cpf'], [1, 'crm', 'cpf'], [3, 'crm', 'cpf']]

lista2 = []

digite = int(input('Digite uma data: '))
for k in range(0, len(lista)):
    if lista[k][0] == digite:
        lista2 += [lista[k]]

for k in range(0, len(lista2)):
    print(lista2[k])

