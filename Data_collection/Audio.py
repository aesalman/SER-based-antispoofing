import os
import glob
import re
import csv
from pydub import AudioSegment
import speech_recognition as sr

def transcribe_audio(audio_path):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        try:
            text = r.recognize_google(audio_data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            text = ""
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            text = ""
    return text

def get_next_file_number(directory):
    files = glob.glob(os.path.join(directory, 'Elon *.wav'))
    if not files:
        return 1
    else:
        highest_num = max(int(re.findall(r'\d+', file)[0]) for file in files)
        return highest_num + 1

def split_audio(file_path, directory):
    start_number = get_next_file_number(directory)
    audio = AudioSegment.from_wav(file_path)
    audio_length_in_ms = len(audio)
    one_min_in_ms = 60 * 1000  # 60 seconds * 1000 ms

    for i, chunk_start in enumerate(range(0, audio_length_in_ms, one_min_in_ms), start=start_number):
        start_time = chunk_start
        end_time = chunk_start + one_min_in_ms
        if end_time > audio_length_in_ms:
            end_time = audio_length_in_ms  # Ensuring last chunk has remaining duration
        
        chunk = audio[start_time:end_time]
        
        chunk_name = os.path.join(directory, f"Elon {str(i).zfill(3)}.wav")
        chunk.export(chunk_name, format="wav")

        transcript = transcribe_audio(chunk_name)

        # Write the filename and transcript to metadata CSV file immediately
        with open(os.path.join(directory, 'metadata.csv'), 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='|')
            writer.writerow([os.path.basename(chunk_name), transcript])

# Replace '/path/to/directory' with your directory path
# And 'path_to_your_audio_file.wav' with the path to your audio file
split_audio('Elon2.wav', 'C:\\Users\\aesal\\OneDrive\\Documents\\Famous Figures\\Elon Musk')