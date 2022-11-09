import time
from datetime import datetime
import pytz

times = {"Western Canada/USA": 'Canada/Pacific', "New Jersey": 'America/New_York',
         "England": "Etc/GMT", "Lebanon": 'Etc/GMT-3', "Sydney": 'Australia/NSW'}

timeline = ""  # LMAO timeline. Im so funni an lonly :(
for zone in times:
    timeline += zone + ": " + datetime.now(pytz.timezone(times[zone])).strftime("%H:%M:%S") + "\n"
    
print(f'24Hr (H:M:S) time in: \n{timeline}')