import os
from pydub import AudioSegment
from pydub.playback import play
from pathlib import Path
from dotenv import load_dotenv , find_dotenv
from openai import OpenAI
from guardian_manager import GuardianManager
import zlib

import pandas as pd
import matplotlib.pyplot as plt
import scipy
import numpy as np

# load dotenv
load_dotenv(find_dotenv())

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

gm = GuardianManager(
    device_id="D6-96-7C-C5-2E-14",
    api_key="idun_2zZuE2ImqssU8T0HnVOlkJNutPXc6q_9nAt0DpTNtrAYgcocAHhEbxoI"
)

def play_audio(text):
    # create crc32 hash of the text
    hashed_text = hex(zlib.crc32(text.encode("utf-8")) & 0xFFFFFFFF)[2:]
    speech_file_path = Path(__file__).parent / f"speeches/speech_{hashed_text}.mp3"

    # check if the file exists, if not create it with openai
    if not speech_file_path.exists():
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

def task_1_record_resting_state():
    play_audio("Please stay still in a rested state for 5 minutes. I will notify you once the recording is complete. Ready?. 3... 2... 1... Recording")
    resting_id = gm.record_data(3)
    play_audio("Recording complete")
    print(f"Downloaded data for recording {resting_id}")
    gm.download_eeg_data(resting_id)
    return resting_id

def task_2_deriving_relative_band_powers():
    pass

def task_3_plotting_relative_band_powers():
    pass

if __name__ == "__main__":
    response = task_0_start_recording()
    if not response:
        gm.disconnect()
        exit()
    task_1_record_resting_state()
    task_2_deriving_relative_band_powers()
    task_3_plotting_relative_band_powers()
    gm.disconnect()

