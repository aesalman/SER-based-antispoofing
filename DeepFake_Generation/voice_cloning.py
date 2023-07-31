import os
import pandas as pd
import sys

from elevenlabs import voices, generate, set_api_key, play, Models, save
sys.path.append("..")
from audio_utils import extract_max_number

from dotenv import load_dotenv
load_dotenv()


def generate_elevenlabs_df(speaker_name, in_script_path, dst_path):

    script_df = pd.read_csv(in_script_path)

    # setting api key for elevenlabs
    elevenlabs_api_key = os.getenv('ELEVELLAB_API_KEY')
    set_api_key(elevenlabs_api_key)

    # check if dst empty
    list_files = os.listdir(dst_path)
    if len(list_files) != 0:
        max_file_num = extract_max_number(list_files, delim=' ')
        script_df = script_df.loc[max_file_num:]

    for id, row in script_df.iterrows():
        filename = row['filename']
        script = row['Transcript']

        print("genearting voice clone of {}".format(filename))

        audio = generate(text=script, voice=speaker_name)

        save(audio, os.path.join(dst_path, filename))


if __name__ == "__main__":

    speaker_name = 'Barack_Obama' # Obama, Trump, Elon Musk, 
    text_file_path = '../Famous_Figures/Test_no_sentiments/Obama_metadata.csv'
    df_type = 'ElevenLabs'
    dst_path = os.path.join('../Famous_Figures/Test_no_sentiments/', speaker_name, df_type) 



    generate_elevenlabs_df(speaker_name, text_file_path, dst_path)