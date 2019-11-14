import asyncio
import time
import random
import string
from random import randrange


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
        latinic = LATINI + (-00.01000)
        longinic = LONGINI + (-00.01000)

        form = Expando()
        form.first_name=''.join(random.choice(letters) for i in range(20))
        form.last_name = ''.join(random.choice(letters) for i in range(20))
        form.nr_residentes = randrange(10)
        form.corrente_nominal = '0.3'
        form.tensao_nominal = '220'
        form.public_building = '0'
        form.latitude = latinic
        form.longitude = longinic
        form.cidade = 'passo fundo'

        print(form.first_name)
        print(form.last_name)
        print(form.nr_residentes)
        print(form.corrente_nominal)
        print(form.tensao_nominal)
        print(form.public_building)
        print(form.latitude)
        print(form.longitude)
        uuid = interscityManager.cadastraRecurso(form)
        print(uuid)
        uuidlist.append(uuidlist)

    while a < 1000:
        selectedUuid = random.choice(letters)
        
    #buscar os valores e jogar no interscity
    


async def main():
    await asyncio.gather(generateValues())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
