import requests
from common.Send import send, Error
import urllib3
import time 
def CampoBot():
    
    time.sleep(15)
    urllib3.disable_warnings()
    control = 0
    lista = []
    newLista = []
    url = "https://segurancainfra.alterdata.matriz/api/"
    urlToSend = 'https://chat.googleapis.com/v1/spaces/AAAADqqXd78/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=4VfSpLl9P4bK7a2mPM4DdhVc5yxfIbDJKZIOBc1kfjc%3D'
    querystring = {"user":"campo.infra","user_cookie":"uiui"}

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic TVRKbU16aG1ZamMzWmpRd1pXSTVZVEV6T0RjeU5EWTNObU00WVRObE1qST06WmpRMVl6QXlOV0kwTldaaU1qQTRZbUpqTWpjeU9Ea3lPR1F6WkRVeE9EUT0="
    }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring, verify=False)
    except:
        print("Ocorreu um erro ao se comunicar com servidor")
        Error(urlToSend)
    dados = response.json()
    for  att in dados:
        idnumber = int(att['IdAtendimento'])
        lista.append(idnumber)
        newLista = set(lista)
    couter = len(newLista)
    for atendimento in dados:
        time.sleep(5)
        send(atendimento, urlToSend)
        control += 1
        if control == couter:
            break



 