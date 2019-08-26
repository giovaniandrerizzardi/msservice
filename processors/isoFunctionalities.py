import interscityManager
import json
from collections import namedtuple

def func71(nr_residentes, co):
    print("funcionalidade 7.1")
    r = interscityManager.getDynamicData('uuid','parametros')
    data = json.loads(r.text, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
    if data.resources == []:
        print ("Nenhum evento neste periodo.")
        return
    infoConsumoList = data.resources[0].capabilities.infoConsumo
    totalEnergy = 0

    for s in infoConsumoList:
        totalEnergy += s.energy_ativa
    energymedium = totalEnergy/nr_residentes
    print("Energia media gasta por residentes: ", energymedium, "kWh")



def func72():
    print("funcionalidade 7.2")

def func73():
    print("funcionalidade 7.3")

def func75():
    print("funcionalidade 7.5")

def func76():
    print("funcionalidade 7.6")

def func77():
    print("funcionalidade 7.7")
