import requests
import json
from datetime import date, datetime, timedelta
from collections import namedtuple
from processors import interscityManager, model

def getALLData():
    url = 'http://localhost:8000/collector/resources/data'
    r = requests.get(url)
    #print(r.text)
    data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    if data.resources == []:
        print ("Nenhum evento neste periodo.")
        return
    infoConsumoList = data.resources[0].capabilities.infoConsumo
    totalDailyEnergy = 0
    print(len(infoConsumoList))
    
    #return r
        
def aaassd():
    uuids = model.casa_info.select()

    response = []

    for casa in uuids:

        r = interscityManager.getDataByUUID(casa.uuid)
        if r.status_code == 200 :   
            data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            if data.resources == []:
                print ("Nenhum evento cadastrado nesta casa.")
            else:
                print('UUID:',casa.uuid, 'numero de eventos: ', len(data.resources[0].capabilities.infoConsumo))
           
        
           
    #print(response)
    #return response

#getALLData()
aaassd()