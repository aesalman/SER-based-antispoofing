from elevenlabs import voices, generate, set_api_key, play

set_api_key("76b67138b806d733c44f4824a468bc29")

voices = voices()

# print(voices)
# print(type(voices))

audio = generate(text="Hi! My name is Bella, nice to meet you!", voice=voices[8])

play(audio)