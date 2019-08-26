from processors import decoder, interscityManager
import json
import requests
dados = decoder.processData_decode("EV_275")
#interscityManager.sendInfoToInterSCity(dados)

datajson = {
        "event_type": dados.Event,
        "energy_ativa": dados.energy_ativa,
        "voltage_real_rms": dados.rmsVoltage_real,
        "phase_real_rms": dados.rmsPhase_real,
        #"total_energy_daily": interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
    }

print (datajson)
requests.post("http://127.0.0.1:1880/attstatus", data=datajson)


print ("OKKKKKKKKKKKKKKKK")
msg = [{
        "channel": "TEMP",
        "dataset": [
            {
                "lon": -52.40667,
                "lat": -28.26278,
                "name": "Casa X",
                "description": "Alerta SOBRETENSÃO ",
                "value": 251,
                "unit": "V",
                "iconColor": "Red"
            },
            {
                "lon": -52.40987,
                "lat": -28.26578,
                "name": "Casa Y",
                "description": "Alerta SOBRETENSÃO ",
                "value": 231,
                "unit": "V",
                "iconColor": "Yellow"
            }
        ]
    }]
datamapjson = {"testemapa": str(msg)}
print (datamapjson)
requests.post("http://127.0.0.1:1880/attmap", data=datamapjson)
#interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
#interscityManager.getDataByRange("9c0772b8-c809-4865-bec7-70dd2013bc37","2018-07-14T14:56:20","2019-07-15T19:56:20")
#a = json.dumps(x)
#print(y)

