import schedule
import time
import requests
import datetime
from url import Website

def refresh_website():
    url = Website
    response = requests.get(url)
    print('refreshed website - status:{response.status_code}')

#schedule the job to run every 10 min
schedule.every(10).minutes.do(refresh_website)
print('refresh successfully' + ' ' + str(datetime.datetime.now()))

#Run the scheduler indefinetely
while True:
    schedule.run_pending()
    time.sleep(1)