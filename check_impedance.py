from idun_guardian_sdk import GuardianBLE
import time

ble = GuardianBLE()

ble.start_impedance(lambda data: print(f"{data}\tOhm"))
time.sleep(10)
ble.stop_impedance()