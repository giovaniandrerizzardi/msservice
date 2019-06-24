import requests
import json

def sendInfoToInterSCity(infos):
    alerts = alertCheck(infos)
    #fazer o send aqui doos alertas, casooo tenha

    data = {}
    alerta = {}
    consumo = {}

    consumo['consumo'] = 'saaa'
    
    data['Alerta'] = alerta
    data['Consumo'] = consumo
    json_data = json.dumps(data)

    requests.post("http://127.0.0.1:8000/capabilities",)
        
    pass


def alertCheck(infos):
    return infos
