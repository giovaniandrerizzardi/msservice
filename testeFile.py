from processors import decoder, interscityManager
import json
import requests

dados = decoder.processData_decode("EV_263", '407da65d-712a-4a8a-b3ca-6eb8e8881374')
interscityManager.sendInfoToInterSCity(dados)

datajson = {
        "event_type": dados.Event,
        "energy_ativa": dados.energy_ativa,
        "voltage_real_rms": dados.rmsVoltage_real,
        "phase_real_rms": dados.rmsPhase_real,
        #"total_energy_daily": interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
    }

print (datajson)
#requests.post("http://127.0.0.1:1880/attstatus", data=datajson)


print ("OKKKKKKKKKKKKKKKK")



#datamapjson = {"testemapa": str(msg2)}
#print (datamapjson)
#requests.post("http://127.0.0.1:1880/attmap", json=str(msg2))
#interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
#interscityManager.getDataByRange("9c0772b8-c809-4865-bec7-70dd2013bc37","2018-07-14T14:56:20","2019-07-15T19:56:20")
#a = json.dumps(x)
#print(y)

