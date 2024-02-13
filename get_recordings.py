from idun_guardian_sdk import GuardianAPI

my_device_id = "E0-53-73-AB-F9-05"
my_api_key = "idun_MWSQ4pkewAGNz8wwYzw_NsweXihLC8tIcFzah8vqqys4Nc-ALzjfTwl2"

api = GuardianAPI(my_device_id, my_api_key)

print(api.get_recordings())