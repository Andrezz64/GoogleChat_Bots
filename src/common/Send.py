# Esta função envia a menssagem para o grupo do google workspace, ele recebe como argumento a URL do espaço e no caso do send(), um JSON com os dados 
import requests
from datetime import datetime

def send(json, url):
    dataatual = datetime.now()
    dataformat = dataatual.strftime('%d/%m/%Y às %H:%M')
    payload = {"text": f"Novo atendimento!\nNúmero: {json['IdAtendimento']}\nUsuário: {json['NmLogin']}\nTipo do atendimento: {json['DsTipoAtendimento']}\nHora: {dataformat}\n{65*'-'}"}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers)

def Error(url): # Envia um erro ao 
    payload = {"text": "Ocorreu um error ao se comunicar com o servidor"}
    headers = {"Content-Type": "application/json"}
    response = requests.request("POST", url, json=payload, headers=headers)
