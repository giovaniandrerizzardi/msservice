import asyncio
import time

async def count():
    a =1
    while a<10:
        
        print("One")
        await asyncio.sleep(1)
    print("Two")


async def generateValues():
    #gerar um UUID 
    #gravar no banco
    #buscar os valores e jogar no interscity
    

    a =1
    while a<10:
        
        print("One")
        await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")