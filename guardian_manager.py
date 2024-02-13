from idun_guardian_sdk import GuardianBLE, GuardianAPI
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
        filename = input("What should the filename be? ")
        self.api.download_recording(recording_id=my_recording_id, eeg=True, imu=False, sleep_report=False, filename=filename)
    def download_sleep_report_data(self, my_recording_id=None):
        if my_recording_id == None:
            recording_json = self.get_recording_json()
            recording_json = dict(recording_json[-1])
            my_recording_id = recording_json["recordingID"]
        filename = input("What should the filename be? ")
        self.api.download_recording(recording_id=my_recording_id, eeg=False, imu=False, sleep_report=True, filename=filename)

    def download_imu_data(self, my_recording_id=None):
        if my_recording_id == None:
            recording_json = self.get_recording_json()
            recording_json = dict(recording_json[-1])
            my_recording_id = recording_json["recordingID"]
        filename = input("What should the filename be? ")
        self.api.download_recording(recording_id=my_recording_id, eeg=False, imu=True, sleep_report=False, filename=filename)

    def record_data(self, duration):
        start_time = datetime.now(timezone.utc)
        while datetime.now(timezone.utc) - start_time < timedelta(seconds=30):
            try:
                time.sleep(1)
            except KeyboardInterrupt:
                break


if __name__ == "__main__":
    guardianManager = GuardianManager()
    while True:
        user_input = input("Enter a function name (check_battery, check_impedance, get_recording_json, download_eeg_data, download_imu_data, download_sleep_report_data), or 'exit' to quit: ")
        
        if user_input == "exit":
            break
        
        if hasattr(guardianManager, user_input):
            getattr(guardianManager, user_input)()
        else:
            print("Invalid function name. Please try again.")
