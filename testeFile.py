from processors import decoder, jsonBuilder
import json
 
dados = decoder.processData_decode("EV_263")

jsonBuilder.sendInfoToInterSCity(dados)

#a = json.dumps(x)
#print(y)
