from cowin_api import CoWinAPI
import os
import sys
import time
import requests
from datetime import datetime

def get(district_id, date, min_age_limit, minimum_slots):

    cowin = CoWinAPI()
    available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)

    options = []
    if len(available_centers['centers']) >= 0:
        for center in available_centers['centers']:
            #print(center['name'])
            for session in center['sessions']:
                if (session['available_capacity'] >= minimum_slots) \
                        and (session['min_age_limit'] <= min_age_limit):
                    out = {
                        'name': center['name'],
                        'district': center['district_name'],
                        'pincode': center['pincode'],
                        'center_id': center['center_id'],
                        'available': session['available_capacity'],
                        'date': session['date'],
                        'slots': session['slots'],
                        'session_id': session['session_id']
                    }
                    options.append(out)

                else:
                    pass
            else:
                pass

    return options

def take_action():
    os.system('beep')
    os.system('beep')
    os.system('beep')
    return True

while True:
    # Input following values before running
    district_id = '363' # Pune
    #district_id = '364' # Akola
    date = '09-05-2021'
    min_age_limit = 18
    minimum_slots = 1

    options = []
    options = get(district_id, date, min_age_limit, minimum_slots)
    if len(options) > 0:
        take_action()
        break
    else:
        refresh_freq = 10
        print(f"============= [{datetime.now()}] Sleeping {refresh_freq} sec ==================")
        for i in range(refresh_freq, 0, -1):
            msg = f"No viable options. Next update in {i} seconds.."
            print(msg, end="\r", flush=True)
            sys.stdout.flush()
            time.sleep(1)

    print('\n')
