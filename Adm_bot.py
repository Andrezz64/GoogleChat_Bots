import requests
from common.Send import send, Error
import urllib3
import time

def AdmBot():
    time.sleep(15)
    urllib3.disable_warnings() # Desabilita Warnings por falta de ssl
# Inicialização de algumas variáveis
    newJson= []
    lista = []
    control = 0
    newLista = []
 # Faz Um get na API do bimer (Filtrada pelo segurança TI )    
    urlToSendAdmin = 'https://chat.googleapis.com/v1/spaces/AAAAkxgVmrE/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=9oJlzGWKxgckVy7A5E_FiAJ3PGd6M67foRamIz93b_A%3D'
    url = "https://segurancainfra.alterdata.matriz/api/"

    querystring = {"user":"infra","user_cookie":"uiui"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic TVRKbU16aG1ZamMzWmpRd1pXSTVZVEV6T0RjeU5EWTNObU00WVRObE1qST06WmpRMVl6QXlOV0kwTldaaU1qQTRZbUpqTWpjeU9Ea3lPR1F6WkRVeE9EUT0="
    }
    try: # envia a requisiçãp
        response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    except:
        print('Erro ao se conectar com o servidor') # Se der um erro envia uma menssagem no Console e para o chat
        Error(urlToSendAdmin)
    dados = response.json()
    for  att in dados:
        idnumber = int(att['IdAtendimento'])
        lista.append(idnumber) # faz a primeira validação, retirando os IDs dos atendimentos repetidos
        newLista = set(lista)
    couter = len(newLista) # conta o numero real de atendimentos na requisição
    print(couter)
    for atendimento in dados:
        newJson.append(atendimento) # faz um novo Json com a quantidade de Atendimentos corrigidos, e as mesmas informações
        control+=1
      
        if control == couter: 
            break

    for att2 in newJson: #  Segundo filtro, dessa vez filtra o novo json, enviando somente os atendimentos do tipo selecionado
        if att2["DsTipoAtendimento"] == 'Logins - Criação' or att2["DsTipoAtendimento"] == 'Logins - Exclusão':
            time.sleep(5)
            send(att2, urlToSendAdmin)
