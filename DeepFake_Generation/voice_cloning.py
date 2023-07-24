import os

from elevenlabs import voices, generate, set_api_key, play

from dotenv import load_dotenv
load_dotenv()

elevenlabs_api_key = os.getenv('ELEVELLAB_API_KEY')

set_api_key(elevenlabs_api_key)

voices = voices()

# print(voices)
# print(type(voices))

audio = generate(text="Hi! My name is Bella, nice to meet you!", voice=voices[9])

play(audio)