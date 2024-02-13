from idun_guardian_sdk import GuardianAPI, GuardianBLE
from datetime import datetime, timezone, timedelta
import time

my_device_id = "E0-53-73-AB-F9-05"
my_api_key = "idun_MWSQ4pkewAGNz8wwYzw_NsweXihLC8tIcFzah8vqqys4Nc-ALzjfTwl2"

ble = GuardianBLE()
api = GuardianAPI(my_device_id, my_api_key)

def intercept_callback(data):
    print(data)

recording_id = api.start_recording(intercept_callback, filtered_stream=True, raw_stream=False)

ble.start_recording(api.callback)

print("Opening recording")
start_time = datetime.now(timezone.utc)
while datetime.now(timezone.utc) - start_time < timedelta(seconds=30):
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break

print("Closing recording")
start_time = datetime.now(timezone.utc)
while datetime.now(timezone.utc) - start_time < timedelta(seconds=30):
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        break


ble.stop_recording()
api.stop_recording()