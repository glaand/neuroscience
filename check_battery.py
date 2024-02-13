from idun_guardian_sdk import GuardianBLE

ble = GuardianBLE("E0:53:73:AB:F9:05")

print(f"Battery: {ble.get_battery()}%")