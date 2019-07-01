import requests
import json
from datetime import date

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__


def sendInfoToInterSCity(dados):
    #alerts = alertCheck(infos)
    #fazer o send aqui doos alertas, casooo tenha
    dados.timestamp = "21/08/2016T10:27:40"
    data = serialize(dados)
    #print(data)
    data2 = {  
        "data":{  
            "Alertas":[  
                {  
                    "alertasobretensao":"1",
                    "alertafuga":"0",
                    "timestamp":"21/08/2016T10:27:40"
                }
            ],
            "Consumos":[  
                {  
                    "Consumo":"24",
                    "ConsumoDia":"10",
                    "timestamp":"21/08/2016T10:27:40"
                }
            ]
        }
    }

   # json_data = json.dumps(data2)
    json_data = json.dumps(data)
    infoConsumo = {"infoConsumo": [data]}
    data3 = {  
        "data":{"infoConsumo": [data]}
    }
    #print(json.dumps(data3))
    r = requests.post('http://127.0.0.1:8000/adaptor/resources/9c0772b8-c809-4865-bec7-70dd2013bc37/data',json=data3)
    print(r.status_code, r.reason)
    print (r.request.body)

def alertCheck(infos):
    return infos

def getDataByUUID(uuid):
    url = 'http://127.0.0.1:8000/collector/resources/' + uuid + '/data'
    r = requests.get(url)
    print(r.text)


#sendInfoToInterSCity("opa")
#getDataByUUID("9c0772b8-c809-4865-bec7-70dd2013bc37")
