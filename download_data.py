from idun_guardian_sdk import GuardianAPI

my_device_id = "E0-53-73-AB-F9-05"
my_api_key = "idun_MWSQ4pkewAGNz8wwYzw_NsweXihLC8tIcFzah8vqqys4Nc-ALzjfTwl2"

api = GuardianAPI(my_device_id, my_api_key)

my_recording_id = "pl-4c3db6fa-9c95-4135-a713-37992a60be02"

print("Downloading recording")
api.download_recording(recording_id=my_recording_id, eeg=True, imu=False, sleep_report=False) 