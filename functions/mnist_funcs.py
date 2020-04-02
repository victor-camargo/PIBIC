from mnist import MNIST
import numpy as np

def load_dataset(s="data"):
    mndata = MNIST('../%s/'%s)
    mndata.gz = True
    X_train, labels_train = map(np.array, mndata.load_training())
    X_test, labels_test = map(np.array, mndata.load_testing())
    #X_train = X_train/255.0
    #X_test = X_test/255.0
    return (X_train, labels_train), (X_test, labels_test)
