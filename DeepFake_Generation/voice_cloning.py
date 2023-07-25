import os
import pandas as pd

from elevenlabs import voices, generate, set_api_key, play, Models

from dotenv import load_dotenv
load_dotenv()

elevenlabs_api_key = os.getenv('ELEVELLAB_API_KEY')

set_api_key(elevenlabs_api_key)

voices = voices()

# print(voices)

models = Models.from_api()

# print(models)

# for i, voice in enumerate(voices):

#     print(i)
#     print(voice)

# print(voices)
# print(type(voices))

# spkr_map = {'Obama': 'Barack_Obama', 'Elon Musk': 'Elon_Musk', 'Trump': 'Donald_Trump'}

speaker_name = 'Barack_Obama' # Obama, Trump, Elon Musk, 
text_file_path = '../Famous_Figures/Test_no_sentiments/ObamaUpdatedmetadata.csv'
dst_path = '../Famous_Figures/Test_no_sentiments/' + speaker_name + 'ElevenLabs/' 

text_pd = pd.read_csv(text_file_path, sep='|')

print(text_pd)

# audio = generate(text="Hi! My name is Bella, nice to meet you!", voice=speaker_name)

# play(audio)