import sys
import os
sys.path.append('./functions')

from deskew import *
from mnist_funcs import *
from thinning import *
import matplotlib.pyplot as plt

from sklearn.preprocessing import OneHotEncoder
from sklearn import linear_model
import sklearn.metrics as metrics

import timeit
import threading
import multiprocessing as mp


def createModel(x,y):
    yp = OneHotEncoder()
    y = yp.fit_transform(y.reshape(60000,1)).toarray()
    clf = linear_model.Ridge (alpha = 0)
    clf.fit(x,y)
    return clf

def predict(model,x):
    return np.argmax(model.predict(x),axis=1)

def image_preprocessing(image):
    
    desk = deskew(image.reshape(28,28)) #Realiza a compensação dos digitos
    ret, thresh = cv2.threshold(desk, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # limiariza usando Otsu
    skel= zhangSuen(thresh) # Aplica a esqueletonização rapida de Zhang-Suen
    return skel


def process_entire_dataset(data, qu, index):
    out = [image_preprocessing(image).flatten() for image in data]
    qu.put(out)
    #print("%d"%index)


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped



def multiprocesses(data, num):
    
    chunks = np.array_split(data, num)
    processes = list()
    fila = mp.Queue()
    
    for i in range(num):
        x = mp.Process(target=process_entire_dataset,args=(chunks[i],fila,i))
        processes.append(x)
        x.start()

    for index, proc in enumerate(processes):
        proc.join()
        print(child.get())
    
    '''
    fila = sorted(fila, key=lambda x:x[1])    
    return np.vstack([np.array(data) for data, index in fila])
    '''

if __name__ == '__main__':
    (X_train, labels_train), (X_test, labels_test) = load_dataset('./data/')
    print('dataset_lido')
    
    testing = X_train[:100]
    wrapped = wrapper(multiprocesses, testing, os.cpu_count())
    timed = timeit.timeit(wrapped,number=1)
    print(timed)
    '''
    X_train_processed = multiprocesses(X_train[:10000], os.cpu_count())
    
    plt.imshow(X_train_processed[0].reshape(28,28),cmap='gray')
    plt.show()
    '''

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
