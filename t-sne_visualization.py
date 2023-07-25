from sklearn.manifold import TSNE
from keras.datasets import mnist
from sklearn.datasets import load_iris
from numpy import reshape
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import numpy as np

from audio_analysis import  gen_speaker_dict


# iris = load_iris()
# x = iris.data
# y = iris.target 

# print(x.shape)
# print(y)

# (x_train, y_train), (_ , _) = mnist.load_data()
# x_train = x_train[:3000]
# y_train = y_train[:3000]
# print(x_train.shape) 
# print(y_train.shape)

# x_mnist = reshape(x_train, [x_train.shape[0], x_train.shape[1]*x_train.shape[2]])
# print(x_mnist.shape)

# x = x_mnist
# y = y_train

##################### Declaractions ########################

speaker_names = ['Barack_Obama', 'Elon_Musk', 'Donald_Trump']
output_path = './output/'


def convert_dict_to_numpy(spkr_dict):
    
    target = []
    spkr_feat = []

    for key in speaker_dict.keys():

        spkr_feat.append(speaker_dict[key])
        
        y = [key]*speaker_dict[key].shape[0]
        target.extend(y)
    
    feat_array = np.vstack(spkr_feat)

    return feat_array, np.array(target)


###################### Extracting Features ##################

x = []
y = np.array([])

for spkr in speaker_names:

    speaker_dict = gen_speaker_dict(spkr, extract_full=True)

    x_feat, y_target = convert_dict_to_numpy(speaker_dict)

    print(x_feat.shape)
    print(y_target.shape)

    x.append(x_feat)
    y = np.concatenate([y, y_target])


x = np.vstack(x)

print(x.shape)
print(y.shape)



###################### Data Set Formatting ##################


# # loading dictionaries
# for spkr in speaker_names:
#     pickle_filename = output_path + spkr + '_test_' + '.pkl'

#     print(spkr)
    
#     with open(pickle_filename, 'rb') as f:
#         spkr_dict = pickle.load(f)

#     print(spkr_dict)

###################### TSNE Visualization ###################

classes = np.unique(y)

tsne = TSNE(n_components=2, verbose=1, random_state=123)

z = tsne.fit_transform(x)

df = pd.DataFrame()
df["y"] = y
df["comp-1"] = z[:,0]
df["comp-2"] = z[:,1]

sns.scatterplot(x="comp-1", y="comp-2", hue=df.y.tolist(),
                palette=sns.color_palette("hls", classes.shape[0]),
                data=df).set(title="Iris data T-SNE projection") 


plt.savefig(output_path + "TSNE_visualization.png", bbox_inches='tight')

plt.show()