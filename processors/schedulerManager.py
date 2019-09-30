#pip install schedule
from processors import interscityManager,isoFunctionalities,model
import schedule
import time
import json
from collections import namedtuple
import requests

iso = isoFunctionalities

def job():
    print("I'm working...")

def dailyProcessing():
    uuid = "9c0772b8-c809-4865-bec7-70dd2013bc37"
    data = interscityManager.getDataDaily(uuid)
    print (data)





schedule.every(1).minutes.do(job)
schedule.every(1).minutes.do(iso.func71)
schedule.every(1).minutes.do(iso.func72)
schedule.every(1).minutes.do(iso.func73)
schedule.every(1).minutes.do(iso.func75)
schedule.every(1).minutes.do(iso.func76)
schedule.every(1).minutes.do(iso.func77)

schedule.every().day.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
