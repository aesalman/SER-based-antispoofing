import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read
import os
from collections import defaultdict
from pathlib import Path
import pickle

from audio_analysis import gen_speaker_dict, plot_speaker_features

############### Declarations #############

# speakers names for which you want to generate the features. 
# Make sure to use the exact same name as the directory name for the speaker data
speaker_names = ['Barack_Obama', 'Elon_Musk', 'Donald_Trump']

# location where the features will be saved
output_path = './output/'
if not os.path.exists(output_path):
    os.mkdir(output_path)

# boolean variables for genrating features and plot
genrate_features = False
generate_plot = True

# generating and saving dictionary
for speaker_name in speaker_names:

    print("Generating and Saving Dictionary for {}".format(speaker_name))
    speaker_pickle_filename = output_path + speaker_name + '_test_' + '.pkl'

    if not os.path.exists(speaker_pickle_filename) or genrate_features:
        speaker_dict = gen_speaker_dict(speaker_name)

        with open(speaker_pickle_filename, 'wb') as f:
            pickle.dump(speaker_dict, f)


########## load the dictionaries #############

# load obama dictioonary
obama_pickle_filename = output_path + 'Barack_Obama' + '_test_' + '.pkl'
with open(obama_pickle_filename, 'rb') as f:
    Obama_dict = pickle.load(f)

# load Musk dictionary
Elon_pickle_filename = output_path + 'Elon_Musk' + '_test_' + '.pkl'
with open(Elon_pickle_filename, 'rb') as f:
    Musk_dict = pickle.load(f)

# load Trump dictioonary
Trump_pickle_filename = output_path + 'Donald_Trump' + '_test_' + '.pkl'
with open(Trump_pickle_filename, 'rb') as f:
    Trump_dict = pickle.load(f)

print("Obama Dict = {} ".format(Obama_dict))

############# Plot Features ###########

if generate_plot:
    plot_speaker_features(Obama_dict, 'Barack Obama', out_dir=output_path)
    plot_speaker_features(Musk_dict, 'Elon Musk', out_dir=output_path)
    plot_speaker_features(Trump_dict, 'Donald Trump', out_dir=output_path)

    plt.show()

    print('Press any button + Enter to close the figures:')
    input()