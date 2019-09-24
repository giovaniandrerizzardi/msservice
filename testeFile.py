from processors import decoder, interscityManager
import json
import requests
dados = decoder.processData_decode("EV_276")
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

msg2 = [
    {
        "channel": "TEMP",
        "dataset": [
            {
                "lon": -3.703548,
                "lat": 40.417204,
                "name": "9fj04r",
                "description": "Temperature in Madrid",
                "value": 20.5,
                "unit": "°C",
                "iconColor": "Blue"
            },
            {
                "lon": -0.075906,
                "lat": 51.508319,
                "name": "04jgpe",
                "description": "Temperature in London",
                "value": 19,
                "unit": "°C",
                "iconColor": "Yellow"
            },
            {
                "lon": 2.34294,
                "lat": 48.859271,
                "name": "lfj82k",
                "description": "Temperature in Paris",
                "label": "Alert for strong frosts",
                "value": 11.7,
                "unit": "°C",
                "iconColor": "Red"
            },
            {
                "lon": 13.402786,
                "lat": 52.517987,
                "name": "0lw233",
                "description": "Temperature in Berlin",
                "value": 10.8,
                "unit": "°C",
                "iconColor": "Red"
            }
        ]
    }

]
#datamapjson = {"testemapa": str(msg2)}
#print (datamapjson)
requests.post("http://127.0.0.1:1880/attmap", json=str(msg2))
#interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
#interscityManager.getDataByRange("9c0772b8-c809-4865-bec7-70dd2013bc37","2018-07-14T14:56:20","2019-07-15T19:56:20")
#a = json.dumps(x)
#print(y)

