import os
from pydub import AudioSegment
from pydub.playback import play

from pathlib import Path
from dotenv import load_dotenv , find_dotenv

from openai import OpenAI

from guardian_manager import GuardianManager

# load dotenv
load_dotenv(find_dotenv())

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

gm = GuardianManager(
    device_id="D6-96-7C-C5-2E-14",
    api_key="idun_2zZuE2ImqssU8T0HnVOlkJNutPXc6q_9nAt0DpTNtrAYgcocAHhEbxoI"
)

def play_audio(text):
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
    )
    response.stream_to_file(speech_file_path)
    music = AudioSegment.from_mp3(speech_file_path)
    play(music)

def task_0_start_recording():
    response = input("Do you want to start recording? (yes/no): ")
    if response.lower() == "yes":
        return True
    else:
        return False

def task_1_record_open_eyes():
    play_audio("Please stay stil and open your eyes and focus on a point in the room for 60 seconds. 3... 2... 1... Recording")
    open_eyes_id = gm.record_data(60)
    gm.download_eeg_data(open_eyes_id)
    return open_eyes_id

def task_2_record_closed_eyes():
    play_audio("Please stay still and close your eyes for 60 seconds. 3... 2... 1... Recording")
    close_eyes_id = gm.record_data(60)
    gm.download_eeg_data(close_eyes_id)
    return close_eyes_id

def task_3_deriving_relative_band_powers():
    pass

def task_4_plotting_relative_band_powers():
    pass


if __name__ == "__main__":
    response = task_0_start_recording()
    if not response:
        exit()
    open_eyes_id = task_1_record_open_eyes()
    close_eyes_id = task_2_record_closed_eyes()
    task_3_deriving_relative_band_powers()
    task_4_plotting_relative_band_powers()
