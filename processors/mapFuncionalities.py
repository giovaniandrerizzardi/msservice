from processors import interscityManager,isoFunctionalities,model
import json
from collections import namedtuple
import requests

def initialMapData():
    uuids = model.casa_info.select(model.casa_info.uuid)

    response = []

    for casa in uuids:
        print (casa.uuid)
        r = interscityManager.getLastDataByUUID(casa.uuid)
        if r.status_code == 200 : 
            data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            if data.resources == []:
                print ("Nenhum evento cadastrado no  intercity.")
                return 0
            else:
                infoConsumoList = data.resources[0].capabilities.infoConsumo
                for dados in infoConsumoList:
                    datajson = {
                        "uuid": dados.uuid,
                        "event_type": dados.Event,
                        "energy_ativa": dados.energy_ativa,
                        "voltage_real_rms": dados.rmsVoltage_real,
                        "phase_real_rms": dados.rmsPhase_real,
                        "lat": -28.26278,
                        "lon": -52.40667,
                        "alert_info": "none"
                        #"total_energy_daily": interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
                    }
                    print("asdasd", dados.energy_ativa)
                    response.append(datajson)
                    break
    print(response)
    requests.post("http://127.0.0.1:1880/initial", json=response)