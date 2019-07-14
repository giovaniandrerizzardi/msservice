from processors import decoder, interscityManager
import json
 
dados = decoder.processData_decode("EV_275")

#interscityManager.sendInfoToInterSCity(dados)


interscityManager.getDataDaily("9c0772b8-c809-4865-bec7-70dd2013bc37")
#a = json.dumps(x)
#print(y)
