import os
import glob
import re
import csv
import pandas as pd
from pydub import AudioSegment
import speech_recognition as sr
import noisereduce as nr

def transcribe_audio(audio_path):
    r = sr.Recognizer()

    with sr.AudioFile(audio_path) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text

def combine_audio_files(input_folder):
    combined_audio = AudioSegment.empty()

    # Iterate through all the files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".wav"):
            input_file = os.path.join(input_folder, filename)

            # Load the input audio using pydub
            audio = AudioSegment.from_file(input_file)

            # Append the audio to the combined audio
            combined_audio += audio

    return combined_audio

def split_audio_into_chunks(audio, chunk_duration, sr=48000):
    metadata = {'filename': [], 'script': []}

    # load the input audio file
    audio = AudioSegment.from_file(input_file)

    # Create an output directory

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # Calculate the total duration of the audio in milliseconds
    total_duration = len(audio)

    # Split the audio into one-minute chunks
    chunk_index = 1
    start_time = 0

    filename_ls = []
    script_ls = []

    while start_time + chunk_duration * 1000 <= total_duration:
        end_time = start_time + chunk_duration * 1000

        # Generate the output filename
        output_file = os.path.join(output_directory, speaker_name + f"_{chunk_index}.wav")

        # Extract the chunk from the audio and export as a single audio file
        chunk = audio[start_time:end_time]
        
        # for noise reduction
        chunk_reduced_noise = nr.reduce_noise(y=chunk, sr=sr)
        chunk_reduced_noise.export(output_file, format="wav")

        transcript = transcribe_audio(output_file)
        # metadata.append([os.path.basename(output_file), transcript])
        filename_ls.append(os.path.basename(output_file))
        script_ls.append(transcript)
        # Update the start time and chunk index for the next chunk
        start_time = end_time
        chunk_index += 1
    # with open(os.path.join(output_directory, 'metadata.csv'), 'w', newline='') as csvfile:
    #     writer = csv.writer(csvfile, delimiter='|')
    #     writer.writerows(metadata)

    # using pandas to write csv files
    metadata['filename'] = filename_ls
    metadata['script'] = script_ls

    metadata_pd = pd.DataFrame(metadata)

    metadata_pd.to_csv(os.path.join(output_directory, 'metadata.csv'))
    

if __name__ == "__main__":
    # input_folder = input("Enter the path to the input folder: ")

    input_folder = "./sample_data/"
    chunk_duration = 60  # in seconds

    # There is no need to combine the audios
    # Combine all the audio files in the input folder
    # combined_audio = combine_audio_files(input_folder)

    input_audio_file = "speaker_A.wav" # speaker_A, speaker_B, speaker_C
    speaker_name = "Obama" # Obama, Elon, Trump etc.

    output_directory = os.path.join(input_folder, speaker_name)

    # Split the combined audio into one-minute chunks
    split_audio_into_chunks(input_audio_file, chunk_duration, speaker_name)