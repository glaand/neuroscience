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

def task_1_record_resting_state():
    play_audio("Please sit still for 5 minutes while we record your resting state data. 3... 2... 1... Recording")
    resting_id = gm.record_data(300)
    gm.download_eeg_data(resting_id)
    return resting_id

def task_2_record_easy_arithmetic():
    play_audio("Please solve the easy arithmetic tasks. 3... 2... 1... Recording")
    easy_id = gm.record_data(300)
    gm.download_eeg_data(easy_id)
    return easy_id

def task_3_record_hard_arithmetic():
    play_audio("Please solve the hard arithmetic tasks. 3... 2... 1... Recording")
    hard_id = gm.record_data(300)
    gm.download_eeg_data(hard_id)
    return hard_id

def task_4_deriving_relative_band_powers():
    pass

def task_5_plotting_relative_band_powers():
    pass


if __name__ == "__main__":
    resting_id = task_1_record_resting_state()
    easy_id = task_2_record_easy_arithmetic()
    hard_i = task_3_record_hard_arithmetic()
    task_4_deriving_relative_band_powers()
    task_5_plotting_relative_band_powers()
