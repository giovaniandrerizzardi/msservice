import requests
import json

def sendInfoToInterSCity(infos):
    alerts = alertCheck(infos)
    #fazer o send aqui doos alertas, casooo tenha

  

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

    json_data = json.dumps(data2)
    print (json_data)
    r = requests.post('http://127.0.0.1:8000/adaptor/resources/9c0772b8-c809-4865-bec7-70dd2013bc37/data',json=data2)
    print(r.status_code, r.reason)
    print (r.request.body)

def alertCheck(infos):
    return infos


sendInfoToInterSCity("opa")