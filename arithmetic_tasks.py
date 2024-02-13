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

#gm = GuardianManager(
#    device_id="E0-53-73-AB-F9-05",
#    api_key="idun_MWSQ4pkewAGNz8wwYzw_NsweXihLC8tIcFzah8vqqys4Nc-ALzjfTwl2"
#)

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

def task_1_record_resting_state():
    play_audio("Please sit still for 5 minutes while we record your resting state data. 3... 2... 1... Recording")
    

def task_2_record_easy_arithmetic():
    play_audio("Please solve the easy arithmetic tasks. 3... 2... 1... Recording")

def task_3_record_hard_arithmetic():
    play_audio("Please solve the hard arithmetic tasks. 3... 2... 1... Recording")

def task_4_deriving_relative_band_powers():
    pass

def task_5_plotting_relative_band_powers():
    pass


if __name__ == "__main__":
    task_1_record_resting_state()
    task_2_record_easy_arithmetic()
    task_3_record_hard_arithmetic()
    task_4_deriving_relative_band_powers()
    task_5_plotting_relative_band_powers()
