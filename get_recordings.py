from idun_guardian_sdk import GuardianAPI

my_device_id = "D6-96-7C-C5-2E-14"
my_api_key = "idun_2zZuE2ImqssU8T0HnVOlkJNutPXc6q_9nAt0DpTNtrAYgcocAHhEbxoI"

api = GuardianAPI(my_device_id, my_api_key)

print(api.get_recordings())