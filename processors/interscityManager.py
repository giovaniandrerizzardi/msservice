import requests
import json
from datetime import date, datetime, timedelta

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__


def sendInfoToInterSCity(dados):
    #alerts = alertCheck(infos)
    
    dados.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = serialize(dados)

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


def getDataDaily(uuid):
    url = 'http://127.0.0.1:8000/collector/resources/' + uuid + '/data'
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S")
    print (now)
    print (yesterday)
    r = requests.get(url, json={'capabilities': [
                     'weather'], 'start_date': yesterday, 'end_date': now})
    print(r.text)
    return r.text


def getDataMonthly(uuid):
    url = 'http://127.0.0.1:8000/collector/resources/' + uuid + '/data'
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    lastMonth = (datetime.now() - timedelta(months=1)
                 ).strftime("%d/%m/%Y %H:%M:%S")
    print(now)
    print(lastMonth)
    r = requests.get(url, json={'capabilities': [
                     'weather'], 'start_date': lastMonth, 'end_date': now})
    print(r.text)
    return r.text

