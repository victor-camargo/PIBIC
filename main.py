import sys
sys.path.append('./functions')

from deskew import *
from mnist_funcs import *
from thinning import *
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn import linear_model
import sklearn.metrics as metrics

def createModel(x,y):
    yp = OneHotEncoder()
    y = yp.fit_transform(y.reshape(60000,1)).toarray()
    clf = linear_model.Ridge (alpha = 0)
    clf.fit(x,y)
    return clf

def predict(model,x):
    return np.argmax(model.predict(x),axis=1)

def image_prepocessing(image):
    
    #img = image.reshape(28,28) #Transforma vetor em uma imagem 28x28
    desk = deskew(image) #Realiza a compensação dos digitos
    desk = cv2.normalize(desk, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1) #Normaliza a imagem para aplicar Otsu
    ret, thresh = cv2.threshold(desk, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # limiariza usando Otsu
    skel= zhangSuen(thresh) # Aplica a esqueletonização rapida de Zhang-Suen

def process_entire_dataset(data):
    processed = []
    for img in range(len(data)):
        process.append(image_preprocessing(img.reshape(28,28)).flatten())
    return np.array(process)


(X_train, labels_train), (X_test, labels_test) = load_dataset('./data/')

model_unchanged = createModel(X_train, labels_train)
acc_train = metrics.accuracy_score(predict(model_unchanged,X_train),labels_train)
acc_test = metrics.accuracy_score(predict(model_unchanged,X_train),labels_test)

print(acc_train)
print(acc_test)
