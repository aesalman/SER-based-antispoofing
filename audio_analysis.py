from disvoice.prosody import Prosody
from phonation import Phonation
from articulation import Articulation


import matplotlib.pyplot as plt
import numpy as np
from scipy.io.wavfile import read
import os
from collections import defaultdict
from pathlib import Path
import pickle

prosody=Prosody()
phonation=Phonation()
articulation=Articulation()

# DATA_DIR = os.path.dirname(os.getcwd()) +  '/audio_data/Famous_Figures/Test/'

DATA_DIR = os.getcwd() +  '/Famous_Figures/Test/'

label_map = {'F0':"frequency (Hz)", 'F1':"frequency (Hz)", 'F2':"frequency (Hz)", 'voiced_rate': 'voiced segments per second',
             'Energy': "Energy (db)", 'jitter': 'variation in periodicity', 'Shimmer': 'micro-instability of vocal cord vibration',
             'F0_derivative':'change in frequency (Hz/s)', 'F1_derivative':'change in frequency (Hz/s)', 'F2_derivative':'change in frequency (Hz/s)'}


def create_list_defaultdict():
    return defaultdict(list)


# generate required features dict
def gen_features_dict(speaker_folder):

    wav_files = list(Path(speaker_folder).glob("**/*.wav"))

    print(wav_files)

    # all_files = os.listdir(speaker_folder)

    # audio_files = []

    # for file in all_files:
        
    #     if file.endswith('.wav'):
    #         audio_files.append(file)

    # audio_files.sort()

    # extract features from the audio files
    features_dict = defaultdict(create_list_defaultdict)

    for wf in wav_files:

        key = wf.parents[0].as_posix().split('/')[-1]
    
        # key = wf.as_posix().split('.')[0].split('_')[0]
        
        filename = wf.as_posix()
        
        print(filename)
        
        prosody_feat = prosody.extract_features_file(filename, static=True, plots=False, fmt="npy")
        phonation_feat = phonation.extract_features_file(filename, static=True, plots=False, fmt="npy")[0]
        articulation_feat = articulation.extract_features_file(filename, static=True, plots=False, fmt="npy")[0] 
        
        
        features_dict[key]['F0'].append(prosody_feat[0])
        features_dict[key]['F1'].append(articulation_feat[116])
        features_dict[key]['F2'].append(articulation_feat[119])
        features_dict[key]['voiced_rate'].append(prosody_feat[78])
        features_dict[key]['Energy'].append(prosody_feat[30])
        features_dict[key]['jitter'].append(phonation_feat[2])
        features_dict[key]['Shimmer'].append(phonation_feat[3])
        features_dict[key]['F0_derivative'].append(phonation_feat[0])
        features_dict[key]['F1_derivative'].append(articulation_feat[117])
        features_dict[key]['F2_derivative'].append(articulation_feat[120])

    return features_dict


# generate speaker dictionary
def gen_speaker_dict(speaker_name):

    speaker_folder = DATA_DIR + speaker_name + '/'

    speaker_folder_ls = os.listdir(speaker_folder)

    print(speaker_folder_ls)

    speaker_dict = defaultdict(dict)

    for df_type in speaker_folder_ls:

        speaker_dict[df_type] = gen_features_dict(speaker_folder + df_type + '/')


    return speaker_dict

# plot speaker features
def plot_speaker_features(speaker_dict, speaker_name, out_dir='./'):

    # generate plots equal to the total number of features
    feature_keys = speaker_dict['Original']['Happy'].keys()
    ncols = 2
    nrows = len(feature_keys) // ncols + (len(feature_keys) % ncols > 0)

    fig, axes = plt.subplots(nrows, ncols, figsize=(50,150))
    fig.subplots_adjust(top=0.5)

    # iterate over the total types of deepfake methods (original, EleveLabs, ...)
    for df_type, feat_dict in speaker_dict.items():

        # print(df_type)
        # print(feat_dict)

        feat_analysis_dict = defaultdict(list)

        # iterate over each feature (F0, F1, F2, voiced_rate, etc)
        for ax, feat_key in zip(axes.flatten(), feature_keys):

            print(feat_key)

            feat_ls, key_ls = zip(*((x, k) for k in feat_dict for x in feat_dict[k][feat_key]))

            # ax[i].plot(key_ls, feat_ls, marker='o', label=df_type + '_' + feat_key)
            ax.plot(key_ls, feat_ls, 'o', markersize=10, label=df_type + '_' + feat_key)
            ax.set_xlabel("Emotion", fontsize=10)
            ax.set_ylabel(label_map[feat_key], fontsize=10)
            ax.tick_params(axis='x', labelsize=10)
            ax.grid(True)
            ax.legend(bbox_to_anchor=(1, 1), loc="upper left", fontsize=8, borderaxespad=0)

    print(fig.dpi)
    
    fig.tight_layout(pad=30, h_pad=50)
    # plt.tight_layout()
    fig.suptitle(speaker_name + " Analysis", fontsize=30, y=1)
    # plt.title(speaker_name + " Analysis", fontsize=30)
    plt.savefig(out_dir + "Barack Obama Analsysis.png", dpi=50, bbox_inches='tight')
    fig.show()




if __name__ == "__main__":
    
    # print(DATA_DIR)

    speaker_names = ['Barack_Obama', 'Elon_Musk', 'Donald_Trump']

    output_path = './output/'

    compute_dict = False

    # generating and saving dictionary Obama
    obama_pickle_filename = output_path + speaker_names[0] + '.pkl'
    if not os.path.exists(obama_pickle_filename) or compute_dict:
        Obama_dict = gen_speaker_dict(speaker_names[0])

        with open(obama_pickle_filename, 'wb') as f:
            pickle.dump(Obama_dict, f)

    # generating and saving dictionary Elon Musk
    Elon_pickle_filename = output_path + speaker_names[1] + '.pkl'
    if not os.path.exists(Elon_pickle_filename) or compute_dict:
        Musk_dict = gen_speaker_dict(speaker_names[1])

        with open(Elon_pickle_filename, 'wb') as f:
            pickle.dump(Musk_dict, f)

    # generating and saving dictionary Elon Musk  
    Trump_pickle_filename = output_path + speaker_names[2] + '.pkl'
    if not os.path.exists(Trump_pickle_filename) or compute_dict:
        Trump_dict = gen_speaker_dict(speaker_names[2])

        with open(Trump_pickle_filename, 'wb') as f:
            pickle.dump(Trump_dict, f)

    # print("Obama Dict = {} ".format(Obama_dict))
    # print("Musk Dict = {} ".format(Musk_dict))

    ########## load the dictionaries #############

    # load obama dictioonary
    with open(obama_pickle_filename, 'rb') as f:
        Obama_dict = pickle.load(f)

    # load Musk dictioonary
    with open(Elon_pickle_filename, 'rb') as f:
        Musk_dict = pickle.load(f)

    # load Trump dictioonary
    with open(Trump_pickle_filename, 'rb') as f:
        Trump_dict = pickle.load(f)

    print("Obama Dict = {} ".format(Obama_dict))

    ############# Plot Features ###########
    plot_speaker_features(Obama_dict, 'Barack Obama', out_dir=output_path)
    plot_speaker_features(Musk_dict, 'Elon Musk', out_dir=output_path)
    plot_speaker_features(Trump_dict, 'Donald Trump', out_dir=output_path)

    print('Press any button + Enter to close the figures:')
    input()
