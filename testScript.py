import asyncio
import time
import random
import string
import requests
from random import randrange
from processors import decoder, alertChecker, model
import time
import multiprocessing as mp

from processors import interscityManager
async def count():
  
    print("One")
    await asyncio.sleep(1)
    print("Two")

LATINI = -28.26278
LONGINI = -52.40667


class Expando(object):
    pass


async def generateValues():
    a = 1
    uuidlist = []
    while a < 1:

        a+=1
        letters = string.ascii_lowercase
        
        latinic = LATINI + (-round(random.uniform(00.00500, 00.03000), 5))
        longinic = LONGINI + (-round(random.uniform(00.00500, 00.03000), 5))
        print(latinic)
        print(longinic)
        form = Expando()
        form.first_name=''.join(random.choice(letters) for i in range(20))
        form.last_name = ''.join(random.choice(letters) for i in range(20))
        form.nr_residentes = randrange(10)
        form.corrente_nominal = '0.3'
        form.tensao_nominal = '220'
        form.public_building = '0'
        form.latitude = latinic
        form.longitude = longinic
        form.cidade = 1

        print(form.first_name)
        print(form.last_name)
        print(form.nr_residentes)
        print(form.corrente_nominal)
        print(form.tensao_nominal)
        print(form.public_building)
        print(form.latitude)
        print(form.longitude)
        #uuid = interscityManager.cadastraRecurso(form, 1)
        #uuid = 'cf7ab1dd-dfc2-400b-b772-d3c3fa4140da'
        #print(uuid)
        #uuidlist.append(uuid)
    uuids = model.casa_info.select()

    response = []

    for casa in uuids:
        #print ('casas ', casa.uuid)
        a = requests.get('http://localhost:8000/catalog/resources/'+ casa.uuid)
        if a.status_code == 200:
            print('achei o uuid no interscity : ', casa.uuid)
            uuidlist.append(casa.uuid)

    print(uuidlist)
    #uuidlist.append('407da65d-712a-4a8a-b3ca-6eb8e8881374')
    #uuidlist.append('d750d04e-b64f-4a56-9b02-6437f795cd84')
    #uuidlist.append('8a571135-9010-4f56-b930-59587de8167a')
    #uuidlist.append('c62824b8-8500-415a-87c8-b4b4906422e5')
    
    #pool = mp.Pool()
    #pool.map(randomGenerate, uuidlist)
    #pool.close()
    print('fechamos ')
    #return 0
    for uuid in uuidlist:
        print("processando uuid: ", uuid)
        
        randomGenerate(uuid)


    while a < 2:
        selectedUuid = random.choice(uuidlist)
        eventCChoice = randrange(2)
        print('selected uuid = ', selectedUuid)
        print('event = ', eventCChoice)
        dados = {}
        if eventCChoice == 0:
            dados = decoder.processData_decode("EV_263", selectedUuid)
        if eventCChoice == 1:
            dados = decoder.processData_decode("EV_275", selectedUuid)
        if eventCChoice == 2:
            dados = decoder.processData_decode("EV_276", selectedUuid)
        
        porcentagemAumentoconsumo = randrange(50)
        porcentagemAumentocorrente = randrange(10)
        porcentagemAumentotensao= randrange(10)
        
        dados.energy_ativa = (dados.energy_ativa + (dados.energy_ativa * porcentagemAumentoconsumo / 100))
        dados.rmsVoltage_real = (dados.rmsVoltage_real + (dados.rmsVoltage_real * porcentagemAumentocorrente / 100))
        dados.rmsPhase_real = (dados.rmsPhase_real + (dados.rmsPhase_real * porcentagemAumentotensao / 100))
        dados.alerta = alertChecker.checkForAlert(dados)
        a += 1
        interscityManager.sendInfoToInterSCity(dados)
        await asyncio.sleep(60)
    #buscar os valores e jogar no interscity
    

def randomGenerate(uuid):
    print("processando uuid: ", uuid)
    a=0
    lastEnergyativa = 0
    while a < 10:
        
        eventCChoice = randrange(1)
        print('EVEnTO = ', eventCChoice)
        dados = {}
        if a == 0:
            dados = decoder.processData_decode("EV_263", uuid)
            dados.energy_ativa = 0.00510000000 #inicia com 0.005 kwh
            lastEnergyativa = dados.energy_ativa
        elif eventCChoice == 0:
            dados = decoder.processData_decode("EV_275", uuid)
        elif eventCChoice == 1:
            dados = decoder.processData_decode("EV_276", uuid)

        porcentagemAumentoconsumo = randrange(20)
        porcentagemAumentocorrente = randrange(10)
        porcentagemAumentotensao = randrange(10)
        print(dados.energy_ativa)
        dados.energy_ativa = lastEnergyativa #recebe o ultimo consumo e adiciona mais  a porcentagem que vai de 0 a 20 %

        dados.energy_ativa = (
            dados.energy_ativa + (dados.energy_ativa * porcentagemAumentoconsumo / 100))
        dados.rmsVoltage_real = (
            dados.rmsVoltage_real + (dados.rmsVoltage_real * porcentagemAumentocorrente / 100))
        dados.rmsPhase_real = (
            dados.rmsPhase_real + (dados.rmsPhase_real * porcentagemAumentotensao / 100))
        dados.alerta = alertChecker.checkForAlert(dados)
        a += 1
        interscityManager.sendInfoToInterSCity(dados)
        print('terminei de postar o evento ')
        time.sleep(1)   #dorme por 20 segundos
    #buscar os valores e jogar no interscity


def basic_func(x):
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'


def multiprocessing_func(x):
    print('asd ', x)
    y = x*x
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))



    


async def main():
    await asyncio.gather(generateValues())
    #dados = interscityManager.getDataByUUID('c62824b8-8500-415a-87c8-b4b4906422e5')
   
    #print(str(dados.text))
if __name__ == "__main__":
    s = time.perf_counter()
    #para o windos, descomenta a linha abaixp e comenta as outras 2
    #asyncio.run(main())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
