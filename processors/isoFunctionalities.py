import interscityManager
import model
import json
from collections import namedtuple

def func71(requestUuid):
    print("funcionalidade 7.1 - O consumo total de energia el ́etrica residencial per capita")
   # r = interscityManager.getDynamicData('uuid','parametros')
    query = []
    if requestUuid == '':
        print("é  para varios uuids")
        query = model.casa_info.select()
    else:
        print("é somente um uuid")
        query = model.casa_info.select().where(model.casa_info.uuid == requestUuid)

    for casa in query:
        energymedium = 0
        print("consultando dados da casa " , casa.uuid, "com ", casa.nr_residentes, " residentes.")
        r = interscityManager.getDataByUUID(casa.uuid)
        if r.status_code == 200 :   
            data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            if data.resources == []:
                print ("Nenhum evento cadastrado nesta casa.")
            else:
                pass
                infoConsumoList = data.resources[0].capabilities.infoConsumo
                totalEnergy = 0

                for s in infoConsumoList:
                    totalEnergy += s.energy_ativa
                print("totalEnergy = ", totalEnergy)
                energymedium = totalEnergy/casa.nr_residentes
            print("Energia media gasta por residentes: ", energymedium, "kWh")

func71('9c0772b8-c809-4865-bec7-70dd2013bc37')

def func72():
    print("funcionalidade 7.2 - Percentagem da populac̃ao da cidade com servico eletrico autorizado(")

def func73():
    print("funcionalidade 7.3 - Consumo de energia de edif́ıcios p ́ublicos por ano(")

def func75():
    print("funcionalidade 7.5 - Uso  total  de  energia  eletrica  per  capita(")

def func76():
    print("funcionalidade 7.6 - Numero m edio de interrupc̃oes eletricas por cliente por ano(")

def func77():
    print("funcionalidade 7.7 - Duração médio de interrupções elétricas")
