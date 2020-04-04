import sys
sys.path.append('./functions')

from deskew import *
from mnist_funcs import *
from thinning import *
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn import linear_model
import sklearn.metrics as metrics
from skimage.filters import threshold_otsu
import timeit

def createModel(x,y):
    yp = OneHotEncoder()
    y = yp.fit_transform(y.reshape(60000,1)).toarray()
    clf = linear_model.Ridge (alpha = 0)
    clf.fit(x,y)
    return clf

def predict(model,x):
    return np.argmax(model.predict(x),axis=1)

def image_preprocessing(image):
    
    #img = image.reshape(28,28) #Transforma vetor em uma imagem 28x28
    desk = deskew(image) #Realiza a compensação dos digitos
    #desk = cv2.normalize(desk, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1) #Normaliza a imagem para aplicar Otsu
    ret, thresh = cv2.threshold(desk, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # limiariza usando Otsu
    skel= zhangSuen(thresh) # Aplica a esqueletonização rapida de Zhang-Suen
    plt.imshow(skel, cmap='gray')
    plt.show()
    return skel

def process_entire_dataset(data):
    processed = []
    for i in range(len(data)):
        processed.append(image_preprocessing(data[i].reshape(28,28)).flatten())
    return np.array(processed)


(X_train, labels_train), (X_test, labels_test) = load_dataset('./data/')
print('dataset_lido')
testing = X_train[:100]

def measure():
    return process_entire_dataset(testing)

#timed = timeit.timeit(measure,number=1)
#print(timed)
image_preprocessing(testing[0].reshape(28,28))










'''
model_unchanged = createModel(X_train, labels_train)#Cria classificador sem preprocessamento
acc_train = metrics.accuracy_score(predict(model_unchanged,X_train),labels_train)
acc_test = metrics.accuracy_score(predict(model_unchanged,X_test),labels_test)

print("Acuracia do treinamento(sem preprocessamento): "+ str(acc_train))
print("Acuracia do teste(sem preprocessamento): "+ str(acc_test))
'''
'''
train_processed = process_entire_dataset(X_train)#trata as imagens de treinamento
test_processed = process_entire_dataset(X_test)#trata as imagens de teste

model_processed = createModel(train_processed, labels_train)#Cria classificador com processamento
acc_train_proc = metrics.accuracy_score(predict(model_processed,train_processed),labels_train)
acc_test_proc = metrics.accuracy_score(predict(model_processed,test_processed),labels_test)

print("Acuracia do treinamento(com preprocessamento): "+ str(acc_train_proc))
print("Acuracia do teste(com preprocessamento): "+ str(acc_tes_proct))
'''
