from processors import decoder, interscityManager
import json
 
dados = decoder.processData_decode("EV_263")

interscityManager.sendInfoToInterSCity(dados)

#a = json.dumps(x)
#print(y)
