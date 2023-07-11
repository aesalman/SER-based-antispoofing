from sklearn.manifold import TSNE
from keras.datasets import mnist
from sklearn.datasets import load_iris
from numpy import reshape
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import pickle


iris = load_iris()
x = iris.data
y = iris.target 

print(x.shape)
print(y)

# (x_train, y_train), (_ , _) = mnist.load_data()
# x_train = x_train[:3000]
# y_train = y_train[:3000]
# print(x_train.shape) 
# print(y_train.shape)

# x_mnist = reshape(x_train, [x_train.shape[0], x_train.shape[1]*x_train.shape[2]])
# print(x_mnist.shape)

# x = x_mnist
# y = y_train


###################### Extracting Features ##################



###################### Data Set Formatting ##################

# speaker_names = ['Barack_Obama', 'Elon_Musk', 'Donald_Trump']
# output_path = './output/'

# # loading dictionaries
# for spkr in speaker_names:
#     pickle_filename = output_path + spkr + '_test_' + '.pkl'

#     print(spkr)
    
#     with open(pickle_filename, 'rb') as f:
#         spkr_dict = pickle.load(f)

#     print(spkr_dict)

###################### TSNE Visualization ###################

# tsne = TSNE(n_components=2, verbose=1, random_state=123)

# z = tsne.fit_transform(x)

# df = pd.DataFrame()
# df["y"] = y
# df["comp-1"] = z[:,0]
# df["comp-2"] = z[:,1]

# sns.scatterplot(x="comp-1", y="comp-2", hue=df.y.tolist(),
#                 palette=sns.color_palette("hls", 3),
#                 data=df).set(title="Iris data T-SNE projection") 

# plt.show()