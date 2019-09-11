import interscityManager
import model
import json
from collections import namedtuple
from peewee import fn
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
            return energymedium
#func71('9c0772b8-c809-4865-bec7-70dd2013bc37')





def func72(cidade):
    print("funcionalidade 7.2 - Percentagem da populac̃ao da cidade com servico eletrico autorizado(")
    querycidade =  model.city_infos.select().where(model.city_infos.city == cidade).dicts().get()
    print(querycidade)
    query = model.casa_info.select(fn.SUM(model.casa_info.nr_residentes)).where(model.casa_info.cidade == querycidade['id']).dicts().get()
    print(query)
    resposta = (query['`nr_residentes`)']*100)/querycidade['nr_habitantes']
    print(" a porcentagem de pessoas com serviço eletrico autorizado em " , querycidade['city'], " é = ", resposta, "%.")
    return resposta
#func72('passo fundo')

#PM389752470BR

def func73():
    print("funcionalidade 7.3 - Consumo de energia de edif́ıcios publicos por ano")
    query = model.casa_info.select().where(model.casa_info.public_building == True)
    totalEnergy = 0
    for casa in query:
        
        print("consultando dados da casa " , casa.uuid, "com ", casa.nr_residentes, " residentes.")
        r = interscityManager.getDataByUUID(casa.uuid)
        if r.status_code == 200 :   
            data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
            if data.resources == []:
                print ("Nenhum evento cadastrado nesta casa.")
                #return 0
            else:
                
                infoConsumoList = data.resources[0].capabilities.infoConsumo

                for s in infoConsumoList:
                    totalEnergy += s.energy_ativa
                print("totalEnergy = ", totalEnergy)
    print("totalEnergy FINAL = ", totalEnergy)
    return totalEnergy
#func73()

def func75():
    print("funcionalidade 7.5 - Uso  total  de  energia  eletrica  per  capita")
    nrresidentes = model.casa_info.select(fn.SUM(model.casa_info.nr_residentes)).dicts().get()
    print(nrresidentes['`nr_residentes`)'])
    r = interscityManager.getALLData()
    if r.status_code == 200 : 
        data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        if data.resources == []:
            print ("Nenhum evento cadastrado no  intercity.")
            return 0
        else:
            pass
            infoConsumoList = data.resources[0].capabilities.infoConsumo
            totalEnergy = 0

            for s in infoConsumoList:
                totalEnergy += s.energy_ativa
            print(totalEnergy)
            total = totalEnergy / float(nrresidentes['`nr_residentes`)'])
            print(total)    
            return total

#func75()       
def func76():
    print("funcionalidade 7.6 - Numero medio de interrupc̃oes eletricas por cliente por ano(")
   
    query = model.casa_info.select()

    for casa in query:
        datajson = {
            "capabilities": [
                "infoConsumo"
            ],
            "matchers": {
                "Event_count_texas.eq": 1
            }
        }         
        r = interscityManager.getDynamicData(casa.uuid, datajson)
        if r.status_code == 200:
            data = json.loads(r.text, object_hook=lambda d: namedtuple(
                'X', d.keys())(*d.values()))
            if data.resources == []:
                print("Nenhum evento cadastrado nesta casa.")
            else:
                infoConsumoList = data.resources[0].capabilities.infoConsumo
        
                print("Numero de interrupcoes = ", len(infoConsumoList))
                return len(infoConsumoList)
#func76()

def func77(requestUuid):
    print("funcionalidade 7.7 - Duração médio de interrupções elétricas")
    query = []
    if requestUuid == '':
        print("é  para varios uuids")
        query = model.casa_info.select()
    else:
        print("é somente um uuid")
        query = model.casa_info.select().where(model.casa_info.uuid == requestUuid)
    
    for casa in query:
        datajson = {
            "capabilities": [
                "infoConsumo"
            ],
            "matchers": {
                "Event_count_texas.eq": 1
            }
        }   

        r = interscityManager.getDynamicData(casa.uuid, datajson)

        if r.status_code == 200:
            data = json.loads(r.text, object_hook=lambda d: namedtuple(
                'X', d.keys())(*d.values()))
            if data.resources == []:
                print("Nenhum evento cadastrado nesta casa.")
            else:
                pass
                infoConsumoList = data.resources[0].capabilities.infoConsumo
                for s in infoConsumoList:
                    print(s.date)

#
#func77('')