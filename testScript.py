import asyncio
import time
import random
import string
from random import randrange
from processors import decoder, alertChecker

from processors import interscityManager
async def count():
    a =1
    while a<10:
        
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
    while a < 2:

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
        uuid = 'c62824b8-8500-415a-87c8-b4b4906422e5'
        print(uuid)
        uuidlist.append(uuid)

    while a < 10:
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
    #buscar os valores e jogar no interscity
    



async def main():
    #await asyncio.gather(generateValues())
    dados = interscityManager.getDataByUUID('c62824b8-8500-415a-87c8-b4b4906422e5')

    print(str(dados.text))
if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
