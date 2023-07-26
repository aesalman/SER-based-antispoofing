import os
import pandas as pd

from elevenlabs import voices, generate, set_api_key, play, Models, save

from dotenv import load_dotenv
load_dotenv()

# print(voices)

# models = Models.from_api()

# # print(models)

# # for i, voice in enumerate(voices):

# #     print(i)
# #     print(voice)

# # print(voices)
# # print(type(voices))

# # spkr_map = {'Obama': 'Barack_Obama', 'Elon Musk': 'Elon_Musk', 'Trump': 'Donald_Trump'}

# speaker_name = 'Barack_Obama' # Obama, Trump, Elon Musk, 
# text_file_path = '../Famous_Figures/Test_no_sentiments/Obamametadata.csv'
# dst_path = '../Famous_Figures/Test_no_sentiments/' + speaker_name + 'ElevenLabs/' 

# text_pd = pd.read_csv(text_file_path)

# print(text_pd)

# audio = generate(text="Hi! My name is Bella, nice to meet you!", voice=speaker_name)

# play(audio)

def generate_elevenlabs_df(speaker_name, in_script_path, dst_path):

    sript_df = pd.read_csv(in_script_path)

    # setting api key for elevenlabs
    elevenlabs_api_key = os.getenv('ELEVELLAB_API_KEY')
    set_api_key(elevenlabs_api_key)

    for id, row in sript_df.iterrows():
        filename = row['Audiofile']
        script = row['Transcript']

        print("genearting voice clone of {}".format(filename))

        # audio = generate(text=script, voice=speaker_name)

        # save(audio, dst_path + filename)


if __name__ == "__main__":

    speaker_name = 'Barack_Obama' # Obama, Trump, Elon Musk, 
    text_file_path = '../Famous_Figures/Test_no_sentiments/Obamametadata.csv'
    df_type = 'ElevenLabs'
    dst_path = os.path.join('../Famous_Figures/Test_no_sentiments/', speaker_name, df_type) 



    generate_elevenlabs_df(speaker_name, text_file_path, dst_path)