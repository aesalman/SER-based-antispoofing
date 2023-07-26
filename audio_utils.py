from pytube import YouTube

from os import path
from pydub import AudioSegment
from pydub.playback import play
import os
import re
from pathlib import Path
from scipy.io import wavfile
import noisereduce as nr

# files                                                                         
src = "transcript.mp3"
dst = "test.wav"

def convert_mp3_to_wav(src, dst):

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")


def extract_number(f):
    s = re.findall("\d+$",f)
    return (int(s[0]) if s else -1,f)

def Download(link, video_save_directory, only_audio=False):
    youtubeObject = YouTube(link)

    if only_audio:
        video_stream = youtubeObject.streams.filter(only_audio = only_audio).first()
    else:

        video_stream = youtubeObject.streams.get_highest_resolution()
    try:
        video_stream.download(video_save_directory)
    except:
        print("Failed to Download Video")

    print("Download is completed successfully")

    return video_stream


def reduce_audio_noise(audio_file, out_file_name = "Emma.wav"):

    sr, audio_data = wavfile.read(audio_file)

    audio_data = audio_data[:,0]

    reduced_noise_audio = nr.reduce_noise(y=audio_data, sr=sr)

    wavfile.write(out_file_name, sr, reduced_noise_audio)

    return reduced_noise_audio




if __name__ == "__main__":

    # src_path = '../audio_data/Famous_Figures/Test/Donald Trump/Eleven Labs/'

    # src_path = os.path.dirname(os.getcwd()) +  '/audio_data/Famous_Figures/Test/'

    # speaker_name = 'Elon_Musk'
    # DF_type = 'ElevenLabs'

    # mp3_fpaths = list(Path(src_path, speaker_name, DF_type).glob("**/*.mp3"))

    # print(mp3_fpaths)

    # # all_files = os.listdir(src_path)

    # # print(all_files)

    # # mp3_files = []

    # for file in mp3_fpaths:
        
    #     # if file.endswith('.mp3'):
    #         # mp3_files.append(file)

    #     filename = file.as_posix().split('.')[0]

    #     print(filename)

    #     # in_file = src_path + file
    #     # out_file = Path(src_path, speaker_name, DF_type) + filename + '.wav'
    #     convert_mp3_to_wav(file.as_posix(), filename + '.wav')

    audio_file = './Famous_Figures/Audio/Shefali/Sophia/Happy/Sofia 04.wav'

    reduced_audio = reduce_audio_noise(audio_file, out_file_name = "Sophia.wav")

