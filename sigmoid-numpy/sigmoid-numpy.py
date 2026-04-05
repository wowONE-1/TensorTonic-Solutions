import numpy as np

def sigmoid(x):

    if type(x) == int or type(x) == list:
        x = np.array(x)

    return 1 / (1 + np.exp(-x))