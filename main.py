from time import sleep
from os import popen as bash, path
from json import loads, dumps
from datetime import datetime as Date
from shutil import which

# ...
if which('speedtest-cli') is None:
    print('\nNão é possível executar este programa. Ele necessita que tenha "speedtest-cli" instalado!\n') # <---
    exit()

# Verifica se o arquivo 'database.json' existe.
# Caso não exista, ele é criado.
if not(path.exists('./database.json')):
    open('./database.json', 'w').write('[]')

# Esta função é responsável por testar a velocidade da internet.
# Ela recebe o código do servidor de teste de conexão (ver lista em "speedtest-cli --list")
# e retorna um float com a velocidade de download em Mbps (sem arredondamento de casas decimais).
# Caso não haja internet ele retorna o resultado 0.0
def InternetTest(server):
    try:
        commandOut_JSON = dict(loads(bash('speedtest-cli --server {0} --json --no-upload'.format(str(server))).read()))
        downloadSpeed_FLOAT = float(commandOut_JSON['download'] / 1000 ** 2)
    except Exception:
        downloadSpeed_FLOAT = 0.0    
    return downloadSpeed_FLOAT

try:
    # Executa o teste de internet duas vezes,
    # o teste é feito em dois servidores
    # diferentes e é tirado a média dos valores.
    downloadSpeed_FLOAT = float((InternetTest(11921) + InternetTest(19903)) / 2)
    
    # Adiciona para as variáveis o mês, dia, hora (formato 24 horas) e minuto, respectivamente.
    month, day, hour, minute = Date.now().strftime("%m,%d,%H,%M").split(',')
    
    # Lê o arquivo JSON String e passa para lista.
    database_LIST = list(loads(open('./database.json', 'r').read()))
    
    # Cria uma lista com os valores [ data, velocidade de download ].
    # A data é armazenada no formato "DD/MM HH:MM".
    end_LIST = [ "{0}/{1} {2}:{3}".format(day, month, hour, minute) , float(round(downloadSpeed_FLOAT, 2)) ]
    
    database_LIST.append(end_LIST)
    
    # Armazena a lista com identação para melhor visualização humana
    # e imprime os valores na tela.
    open('./database.json', 'w').write(str(dumps(database_LIST, indent=4)))
    print(end_LIST)
except Exception as error:
    # Este except armazena qualquer erro para um arquivo "error.log", e o exibe na tela
    open('./error.log', 'a').write( str(error) + '\n\n')
    print(error)