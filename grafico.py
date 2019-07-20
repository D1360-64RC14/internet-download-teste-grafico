import matplotlib.pyplot as plt
from json import loads as parseJson
from re import search as RegEx

# Lê o arquivo "database.json" em forma de lista.
database = parseJson(open('./database.json', 'r').read())

# ...
if len(database[0]) == 0:
    print('\n Não há dados no banco de dados!\n') # <---
    exit()

# Organiza a lista de datas.
Datas = []
for z in range(len(database)):
    if database[z][0].split(' ')[0] not in Datas:
        Datas.append(database[z][0].split(' ')[0])
print('\n Datas disponíveis para pesquisa:\n {0}\n'.format(str(Datas).strip('[]')))

# Primeiro print.
# O IF e ELIF são responsáveis por verificar
# se o valor foi digitado corretamente.
print(' Selecione uma data (ou apenas aperte [enter] para continuar):')
matchData = input(' :: DD/MM :: ').strip()
if not(RegEx("\d\d\/\d\d", str(matchData)) or matchData == ''): print('\n Digite uma data no formato DD/MM!\n'); exit()
elif not(matchData in Datas or matchData == ''): print('\n Esta data não está na lista!\n'); exit()
print()

# Segundo print
print(' Selecione uma hora (ou apenas aperte [enter] para continuar):')
matchDia = input(' :: HH :: ').strip()
if not(RegEx("\d\d", str(matchDia)) or matchDia == ''): print('\n Digite uma hora no formato HH!\n'); exit()
elif not(0 <= (int(matchDia) if matchDia else 0) <= 23 or matchDia == ''): print('\n Esta hora não é válida!\n'); exit()
print()

# Variáveis para funcionamento
# do matplotlib
X, Y, suptitle = [], [], ''

# Esta condição é executada caso
# o usuário informe uma data.
if matchData:
    
    # Este bloco separa apenas
    # os dados com a data informada.
    databaseNew = []
    for z in range(len(database)):
        if database[z][0].split(' ')[0] == matchData:
            databaseNew.append(database[z])
    database = databaseNew

    # Label e título informando
    # o dia selecionado
    plt.xlabel("Horas")
    suptitle = 'Gráfico de Velocidade de Internet\nDia: {0}'.format(matchData)
else:
    suptitle = 'Gráfico de Velocidade de Internet\nDia: todos'
    plt.xlabel("Dias/Horas")

# Esta função é executada caso
# o usuário informe um dia.
if matchDia:
    
    # Este bloco de código separa apenas
    # os dados com o dia informado.
    databaseNew = []
    for z in range(len(database)):
        if int(database[z][0].split(' ')[1].split(':')[0]) == int(matchDia):
            databaseNew.append(database[z])
    database = databaseNew
    
    # Adiciona ao título
    # o dia informado
    suptitle += '; Hora: {0}:00'.format(matchDia)

# Caso nenhuma informação for encontrada o programa se
# encerra, pois não teria valores para montar o gráfico.
if len(database) == 0:
    print(' Esta hora não está presente na lista!\n')
    exit()

# Este bloco separa o valor
# selecionado para criar o gráfico.
for z in range(len(database)):
    X.append(database[z][0].split(' ')[1]) if matchData else X.append(database[z][0])
    Y.append(database[z][1])

# Coloca o valor em cima de cada ponto.
# (Este aqui não fui eu que fiz)
for z, data in enumerate(Y):
    plt.text(x=z - 0.15, y=data + 0.4, color="#283593", s=str(data))

# Maioria das configurações do matplotlib.
plt.plot(X, Y, marker='.', ms=10, lw=2.5, color='#283593')
plt.ylabel("Velocidade (Mbps)")
plt.suptitle(suptitle)
plt.grid(True)
plt.ylim(0, 20)

# Mostra o gráfico.
plt.show()