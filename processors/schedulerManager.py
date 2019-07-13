#pip install schedule
import schedule
import time
import interscityManager


def job():
    print("I'm working...")

def dailyProcessing():
    uuid = "9c0772b8-c809-4865-bec7-70dd2013bc37"
    data = interscityManager.getDataDaily(uuid)
    print (data)

schedule.every(1).minutes.do(job)
schedule.every().day.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
