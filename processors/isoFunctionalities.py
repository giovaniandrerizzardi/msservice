import interscityManager
import model
import json
from collections import namedtuple

def func71(nr_residentes, co):
    print("funcionalidade 7.1 - O consumo total de energia el ́etrica residencial per capita")
   # r = interscityManager.getDynamicData('uuid','parametros')
    query = model.casa_info.select()
    for casa in query:
        energymedium = 0
        print("consultando dados da casa " , casa.uuid)
        r = interscityManager.getDataByUUID(casa.uuid)
        data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        if data.resources == []:
            print ("Nenhum evento cadastrado nesta casa.")
        else:
            pass
            infoConsumoList = data.resources[0].capabilities.infoConsumo
            totalEnergy = 0

            for s in infoConsumoList:
                totalEnergy += s.energy_ativa
            energymedium = totalEnergy/nr_residentes
        print("Energia media gasta por residentes: ", energymedium, "kWh")



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
