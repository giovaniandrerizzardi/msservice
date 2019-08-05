import requests
import json
from datetime import date, datetime, timedelta
from collections import namedtuple

def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__


def sendInfoToInterSCity(dados):
    #alerts = alertCheck(infos)
    
    dados.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = serialize(dados)
    print("aaaaaaaaaaaaaaaaaaaaa")
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
    uuid = "9c0772b8-c809-4865-bec7-70dd2013bc37"
    url = 'http://127.0.0.1:8000/collector/resources/' + uuid + '/data'
    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S")
    print ("Get Daily Energy information with range ", yesterday, " until ", now)
    r = requests.post(url, json={'start_date': yesterday, 'end_date': now})
   
    data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    infoConsumoList = data.resources[0].capabilities.infoConsumo
    totalDailyEnergy = 0
   
    for s in infoConsumoList:
        totalDailyEnergy += s.energy_ativa
  
    print ("Daily total energy: ", totalDailyEnergy, "kWh")

    #print(r.text)
    return totalDailyEnergy


def getDataByRange(uuid, startDate, endDate):
    uuid = "9c0772b8-c809-4865-bec7-70dd2013bc37"
    url = 'http://127.0.0.1:8000/collector/resources/' + uuid + '/data'
    print ("Get Energy information with range ", startDate, " until ", endDate)
    r = requests.post(url, json={'start_date': startDate, 'end_date': endDate})
   
    data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    infoConsumoList = data.resources[0].capabilities.infoConsumo
    totalDailyEnergy = 0
    for s in infoConsumoList:
        totalDailyEnergy += s.energy_ativa
   
    print ("Daily total energy: ", totalDailyEnergy, "kWh")

    #print(r.text)
    return totalDailyEnergy


def postDynamicData(uuid, parameterString):
    url = 'http://127.0.0.1:8000/collector/resources/'
    if uuid != '':
        url +=uuid + '/data'
    else :
        url += '/data'

    print (parameterString)
    print (url)


def getDynamicData(uuid, parameterString):
    url = 'http://127.0.0.1:8000/collector/resources/'
    if uuid != '':
        url +=uuid + '/data'
    else :
        url += '/data'

  #  if parameterString != None :
   #     url+= '/'+parameterString
    print (url)
    r = requests.post(url, json=parameterString)
    print (r.text)
#olhar o online playgroud pra colocar o json  dinamico aqui
#getDynamicData('9c0772b8-c809-4865-bec7-70dd2013bc37','{start_date":"2019-07-14T14:56:20","end_date":"2019-07-16T14:56:20"}')