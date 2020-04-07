from sklearn.preprocessing import OneHotEncoder
from sklearn import linear_model
import sklearn.metrics as metrics
import numpy as np
def createModel(x,y):
    yp = OneHotEncoder()
    y = yp.fit_transform(y.reshape(60000,1)).toarray()
    clf = linear_model.Ridge (alpha = 0)
    clf.fit(x,y)
    return clf

def predict(model,x):
    return np.argmax(model.predict(x),axis=1)
