import requests
import json
from datetime import date, datetime

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__


def sendInfoToInterSCity(dados):
    #alerts = alertCheck(infos)
    
    dados.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = serialize(dados)

   # json_data = json.dumps(data2)
   # json_data = json.dumps(data)
   # infoConsumo = {"infoConsumo": [data]}
    infoConsumo = {  
        "data":{"infoConsumo": [data]}
    }
   # print(infoConsumo)
    #print(json.dumps(infoConsumo))
    r = requests.post('http://127.0.0.1:8000/adaptor/resources/9c0772b8-c809-4865-bec7-70dd2013bc37/data',json=infoConsumo)
    print(r.status_code, r.reason)
    print (r.request.body)

def alertCheck(infos):
    return infos

def getDataByUUID(uuid):
    url = 'http://127.0.0.1:8000/collector/resources/' + uuid + '/data'
    r = requests.get(url)
    print(r.text)

