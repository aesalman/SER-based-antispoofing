import os
import glob
import re
import csv
import pandas as pd
import numpy as np
from pydub import AudioSegment
from scipy.io import wavfile
import speech_recognition as sr
import noisereduce as nr

import sys
sys.path.append("..")
from audio_utils import extract_max_number

def transcribe_audio(audio_path):
    r = sr.Recognizer()

    try:
        with sr.AudioFile(audio_path) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        print(f"Could not transcribe {audio_path}. UnknownValueError.")
        return ""

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

def split_audio_into_chunks(input_folder, input_file, chunk_duration, speaker_name, sr=48000):
    metadata = {'filename': [], 'Transcript': []}

    # load the input audio file
    audio = AudioSegment.from_file(input_folder + input_file)
    audio_data = audio.set_channels(1)

    print(audio_data)

    # sr, audio_data = wavfile.read(input_file)
    # audio_data = audio_data[:,0]

    # Create an output directory
    output_directory = os.path.join(input_folder, speaker_name)
    noise_out_dir = os.path.join(input_folder, speaker_name + '_reduced_noise')

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
        base_index = 0
    else:
        list_files = os.listdir(output_directory)
        print(list_files)
        base_index = extract_max_number(list_files)
        # base_index = max(list_files, key=extract_number)

    # if not os.path.exists(noise_out_dir):
    #     os.makedirs(noise_out_dir)

    # Calculate the total duration of the audio in milliseconds
    total_duration = len(audio_data)

    print(total_duration)

    # Split the audio into one-minute chunks
    chunk_index = 1
    start_time = 0

    filename_ls = []
    script_ls = []


    while start_time + chunk_duration * 1000 <= total_duration:
        end_time = start_time + chunk_duration * 1000

        print("Generating Chunk File {}".format(chunk_index))
        
        # Generate the output filename
        file_index = base_index + chunk_index
        output_file = os.path.join(output_directory, speaker_name + f"_{file_index}.wav")
        # output_file_reduced_noise = os.path.join(noise_out_dir, speaker_name + f"_{chunk_index}.wav")

        # Extract the chunk from the audio and export as a single audio file
        chunk = audio_data[start_time:end_time]
        chunk.export(output_file, format="wav")
        
        # for noise reduction
        # chunk_array = np.array(chunk.get_array_of_samples())
        # chunk_reduced_noise = nr.reduce_noise(y=chunk_array, sr=sr)
        # chunk_reduced_noise.export(output_file_reduced_noise, format="wav")

        try:
            transcript = transcribe_audio(output_file)

         # Skip this file if the transcript is empty
            if len(transcript) == 0:
                print(f"Skipping file {output_file} due to empty transcript")
            else:
                # Append to metadata only if transcript is not empty
                filename_ls.append(os.path.basename(output_file))
                script_ls.append(transcript)

        except sr.UnknownValueError:
                print(f"Skipping file {output_file} due to UnknownValueError")

        # Update the start time and chunk index for the next chunk
        start_time = end_time
        chunk_index += 1

    # using pandas to write csv files
    metadata['filename'] = filename_ls
    metadata['Transcript'] = script_ls

    metadata_pd = pd.DataFrame(metadata)

    # metadata csv filename
    output_csv = os.path.join(input_folder, speaker_name + '_metadata.csv')

    if os.path.exists(output_csv):
        base_metadata = pd.read_csv(output_csv)
    
        metadata_pd = pd.concat([base_metadata, metadata_pd])

    metadata_pd.to_csv(output_csv, index=False)
    

if __name__ == "__main__":
    # input_folder = input("Enter the path to the input folder: ")

    input_folder = "./sample_data/data/"
    chunk_duration = 60  # in seconds

    # There is no need to combine the audios
    # Combine all the audio files in the input folder
    # combined_audio = combine_audio_files(input_folder)

    input_audio_file = "speaker_D.wav" # speaker_A, speaker_B, speaker_C
    speaker_name = "Trump" # Obama, Elon, Trump etc.

    # Split the combined audio into one-minute chunks
    split_audio_into_chunks(input_folder, input_audio_file, chunk_duration, speaker_name)
