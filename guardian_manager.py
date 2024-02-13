from idun_guardian_sdk import GuardianBLE, GuardianAPI
from datetime import datetime, timezone, timedelta
import time

class GuardianManager:
    def __init__(self, device_id, api_key):
        self.ble = GuardianBLE()
        self.api = GuardianAPI(device_id, api_key)

    def check_battery(self):
        print(f"Battery: {self.ble.get_battery()}%")

    def check_impedance(self):
        self.ble.start_impedance(lambda data: print(f"{data}\thOhm"))
        time.sleep(10)
        self.ble.stop_impedance()

    def get_recording_json(self):
        return list(self.api.get_recordings())

    def download_eeg_data(self, my_recording_id=None):
        if my_recording_id == None:
            recording_json = self.get_recording_json()
            recording_json = dict(recording_json[-1])
            my_recording_id = recording_json["recordingID"]
        self.api.download_recording(recording_id=my_recording_id, eeg=True, imu=False, sleep_report=False, filename=f"{my_recording_id}_eeg.csv")

    def download_sleep_report_data(self, my_recording_id=None):
        if my_recording_id == None:
            recording_json = self.get_recording_json()
            recording_json = dict(recording_json[-1])
            my_recording_id = recording_json["recordingID"]
        self.api.download_recording(recording_id=my_recording_id, eeg=False, imu=False, sleep_report=True, filename=f"{my_recording_id}_sleep_report.csv")

    def download_imu_data(self, my_recording_id=None):
        if my_recording_id == None:
            recording_json = self.get_recording_json()
            recording_json = dict(recording_json[-1])
            my_recording_id = recording_json["recordingID"]
        self.api.download_recording(recording_id=my_recording_id, eeg=False, imu=True, sleep_report=False, filename=f"{my_recording_id}_imu.csv")

    def record_data(self, duration):
        recording_id = self.api.start_recording(None, filtered_stream=None, raw_stream=False)
        self.ble.start_recording()

        start_time = datetime.now(timezone.utc)
        while datetime.now(timezone.utc) - start_time < timedelta(seconds=duration):
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break


        self.ble.stop_recording()
        self.api.stop_recording()

        return recording_id
