from pydub import AudioSegment
import math
import os

class SplitWavAudioMubin():
    def __init__(self, folder, filename, out):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + filename
        self.out = out
        
        self.audio = AudioSegment.from_file(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        t1 = from_min * 60 * 1000
        t2 = to_min * 60 * 1000
        split_audio = self.audio[t1:t2]
        out_folder = self.folder + self.out
     
        if not os.path.exists(out_folder):
            os.makedirs(out_folder)

        split_audio.export(out_folder + split_filename, format="wav")
        
    def multiple_split(self, min_per_split):
        total_mins = math.ceil(self.get_duration() / 60)
        for i in range(0, total_mins, min_per_split):
            filename_without_ext = self.filename.split('.')
            split_fn = str(i) + '_' + filename_without_ext[0]
            self.single_split(i, i+min_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_mins - min_per_split:
                print('All splited successfully')



if __name__ == "__main__":

    speaker_name = 'Barack Obama/'
    folder = './output/' + speaker_name
    
    file = 'Obama speech after Donald Trump claims US election victory.mp4'

    output_folder = 'split_audio_files/'

    split_wav = SplitWavAudioMubin(folder, file, output_folder)
    # print(split_wav.audio)
    split_wav.multiple_split(min_per_split=1)