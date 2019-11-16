from processors import interscityManager,isoFunctionalities,model
import json
from collections import namedtuple
import requests

def initialMapData():
    uuids = model.casa_info.select()

    response = []

    for casa in uuids:
        print ('casas ', casa.uuid)


    for casa in uuids:
        print (casa.uuid)
        dados = interscityManager.getLastDataByUUID(casa.uuid)
        
        if dados is None:
            print('nao tem dados')
        else:
            print (dados.alerta)
            datajson = {
                "uuid":casa.uuid,
                "event_type": dados.Event,
                "energy_ativa": round(float(dados.energy_ativa), 5),
                "voltage_real_rms": round(float(dados.rmsVoltage_real), 2),
                "phase_real_rms": round(float(dados.rmsPhase_real), 2),
                "lat": float(casa.latitude),
                "lon": float(casa.longitude),
                "alert_info": dados.alerta
                #"total_energy_daily": interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
            }
        
            response.append(datajson)
            #break
    #print(response)
    return response
    #requests.post("http://127.0.0.1:1880/initial", json=response)


def initialMapDatdddddda():
    uuids = model.casa_info.select()

    response = []

    for casa in uuids:
        print(casa.uuid)
        r = interscityManager.getLastDataByUUID(casa.uuid)
        if r.status_code == 200:
            data = json.loads(r.text, object_hook=lambda d: namedtuple(
                'X', d.keys())(*d.values()))
            if data.resources == []:
                print("Nenhum evento cadastrado no  intercity.")
                return 0
            else:
                infoConsumoList = data.resources[0].capabilities.infoConsumo
                for dados in infoConsumoList:
                    print(casa.latitude)
                    datajson = {
                        "uuid": casa.uuid,
                        "event_type": dados.Event,
                        "energy_ativa": round(float(dados.energy_ativa), 2),
                        "voltage_real_rms": round(float(dados.rmsVoltage_real), 2),
                        "phase_real_rms": round(float(dados.rmsPhase_real), 2),
                        "lat": float(casa.latitude),
                        "lon": float(casa.longitude),
                        "alert_info": "none"
                        #"total_energy_daily": interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
                    }
                    print("asdasd", dados.energy_ativa)
                    response.append(datajson)
                    break
    print(response)
    return response
    #requests.post("http://127.0.0.1:1880/initial", json=response)
