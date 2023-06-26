import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

samples = make_classification(n_samples=1000, n_features=2, n_redundant=0, n_informative=1, n_clusters_per_class=1, flip_y=-1)
red = samples[0][samples[1] == 0]
blue = samples[0][samples[1] == 1]
red_labels = np.zeros(len(red))
blue_labels = np.ones(len(blue))
labels = np.append(red_labels, blue_labels)
inputs = np.concatenate((red, blue), axis=0)

x_train, x_test, y_train, y_test = train_test_split(inputs, labels, test_size=0.33, random_state=42)

def sigmoid(t_):
    return 1 / (1+np.exp(-t_))