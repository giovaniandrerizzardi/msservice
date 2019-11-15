import requests
import json
from datetime import date, datetime, timedelta
from collections import namedtuple
from processors import model, environmentVariables


def serialize(obj):
    if isinstance(obj, date):
        serial = obj.isoformat()
        return serial

    return obj.__dict__


def sendInfoToInterSCity(dados):
    #alerts = alertCheck(infos)
    
    print("Adicionando o ultimo evento no banco")
    lastEvent = {}
    newEventId = 0
    try:
        print(dados.uuid)
        lastEvent = model.last_event.select().where(model.last_event.uuid == dados.uuid).order_by(model.last_event.id_evento.desc()).get()
        print('o ultimo evento foi : ', lastEvent)
        newEventId = lastEvent.id_evento + 1
        consumoEvento = round(float(dados.energy_ativa) - lastEvent.total_consume, 5)
        dados.specific_energy_ativa = consumoEvento
    except model.last_event.DoesNotExist:
        print("DATA NOT FOUND")
        consumoEvento = 0.0
        dados.specific_energy_ativa = dados.energy_ativa

    

    if dados.alerta == 'none':
        model.add_event(newEventId, dados.uuid, consumoEvento, False)
    else:
        model.add_event(newEventId, dados.uuid, consumoEvento, True)

    print('Evento atual:  ', newEventId)
    dados.Event_count_texas_tot = newEventId
    #return
    dados.timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    data = serialize(dados)
    print("enviando os dados do evento numero " + str(dados.Event_count_texas_tot))
    infoConsumo = {  
        "data":{"infoConsumo": [data]}
    }
    
    #url = 'http://127.0.0.1:8000/adaptor/resources/'+ dados.uuid + '/data'
    url = environmentVariables.INTERSCITY_MAIN_URL+'/adaptor/resources/' + dados.uuid + '/data'
    print(url)
    r = requests.post(url,json=infoConsumo)
    print(r.status_code, r.reason)
    if r.status_code != 200 :
        return
    print (r.request.body)

def getLastDataByUUID(uuid):
    url = environmentVariables.INTERSCITY_MAIN_URL + '/collector/resources/' + uuid + '/data/last'
    print(url)
    r = requests.get(url)
    data = json.loads(r.text, object_hook=lambda d: namedtuple(
        'X', d.keys())(*d.values()))
    if data.resources == []:
        print("Nenhum evento neste periodo.")
        return
    infoConsumoList = data.resources[0].capabilities.infoConsumo

    for s in infoConsumoList:
        return s
    


def alertCheck(infos):
    return infos

def getDataByUUID(uuid):
    url = environmentVariables.INTERSCITY_MAIN_URL + '/collector/resources/' + uuid + '/data'
    r = requests.get(url)
    #print(r.text)
    return r

def getALLData():
    url = environmentVariables.INTERSCITY_MAIN_URL + '/collector/resources/data'
    r = requests.get(url)
    #print(r.text)
    return r

def getDataDaily(uuid):
    #uuid = "9c0772b8-c809-4865-bec7-70dd2013bc37"

    url = environmentVariables.INTERSCITY_MAIN_URL +'/collector/resources/' + uuid + '/data'

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    yesterday = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y %H:%M:%S")
   
    print ("Get Daily Energy information with range ", yesterday, " until ", now)
    
    r = requests.post(url, json={'start_date': yesterday, 'end_date': now})
   
    data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    if data.resources == []:
        print ("Nenhum evento neste periodo.")
        return
    infoConsumoList = data.resources[0].capabilities.infoConsumo
    totalDailyEnergy = 0
   
    for s in infoConsumoList:
        totalDailyEnergy += s.energy_ativa
  
    print ("Daily total energy: ", totalDailyEnergy, "kWh")

    #print(r.text)
    return totalDailyEnergy



def getDataByRange(uuid, startDate, endDate):
    #uuid = "9c0772b8-c809-4865-bec7-70dd2013bc37"
    url = environmentVariables.INTERSCITY_MAIN_URL + \
        '/collector/resources/' + uuid + '/data'
    print ("Get Energy information with range ", startDate, " until ", endDate)
    r = requests.post(url, json={'start_date': startDate, 'end_date': endDate})
    if r.status_code > 299:
        print('algum erro ocorreu no interscity')
        return 0

    data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    if data.resources == []:
        print ("Nenhum evento neste periodo.")
        return
    infoConsumoList = data.resources[0].capabilities.infoConsumo
    
    return infoConsumoList


def postDynamicData(uuid, parameterString):
    url = environmentVariables.INTERSCITY_MAIN_URL + '/collector/resources/'
    if uuid != '':
        url +=uuid + '/data'
    else :
        url += '/data'

    print (parameterString)
    print (url)


def getDynamicData(uuid, parameterString):
    url = environmentVariables.INTERSCITY_MAIN_URL + '/collector/resources/'
    if uuid != '':
        url +=uuid + '/data'
    else :
        url += '/data'

    print('buscando dados dinamicos com o json ', parameterString)
    print (url)
    r = requests.post(url, json=parameterString)
    #print (r.text)
    return r

def getResourceByUuid(uuid):
    print("Buscando um recurso pelo uuid -> ", uuid)
    r = requests.get(
        environmentVariables.INTERSCITY_MAIN_URL + '/catalog/resources/'+uuid)
    print(r.text)
    return r

def cadastraRecurso(form,istest):
    if istest == 1:
        first_name = form.first_name
        last_name = form.last_name
        nr_residentes = int(form.nr_residentes)
        corrente_nominal = form.corrente_nominal
        tensao_nominal = form.tensao_nominal
        public_building = bool(form.public_building)
        latitude = float(form.latitude)
        longitude = float(form.longitude)
        cidade= int(form.cidade)
        senha = '123456789'
    else:
        first_name = form.first_name.data
        last_name = form.last_name.data
        nr_residentes = int(form.nr_residentes.data)
        corrente_nominal = form.corrente_nominal.data
        tensao_nominal = form.tensao_nominal.data
        public_building = bool(form.public_building.data)
        latitude = float(form.latitude.data)
        longitude = float(form.longitude.data)
        cidade = int(form.cidade.data)
        senha = '123456789'
    
    description = 'Casa do:'+ first_name + ' ' + last_name
    data = {
        "data": {
            "lat": latitude,
            "lon": longitude,
            "description": description,
            "capabilities": [
                "infoConsumo"
            ],
            "status": "active"
        }
    }
    url = environmentVariables.INTERSCITY_MAIN_URL + '/catalog/resources'
    response = requests.post(url,json=data)

    print(response.text)
    data = json.loads(response.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))

    model.addcasa_info(data.data.uuid, senha, nr_residentes, corrente_nominal, public_building,tensao_nominal,latitude,longitude,cidade)
    return data.data.uuid
    #e62100d7-7d80-4c1c-a7fe-477813c15e21

#getResourceByUuid('30b057a1-a28a-4460-8784-77ba0f0801f9')
