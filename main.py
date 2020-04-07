import sys
sys.path.append('./functions')

import matplotlib.pyplot as plt
from image_processing import *
from classifier_funcs import *


(X_train, labels_train), (X_test, labels_test) = load_dataset('./data/')


model_unchanged = createModel(X_train, labels_train)#Cria classificador sem preprocessamento
acc_train = metrics.accuracy_score(predict(model_unchanged,X_train),labels_train)
acc_test = metrics.accuracy_score(predict(model_unchanged,X_test),labels_test)

print("Acuracia do treinamento(sem preprocessamento): "+ str(acc_train))
print("Acuracia do teste(sem preprocessamento): "+ str(acc_test))


train_processed = process_entire_dataset(X_train)#trata as imagens de treinamento
test_processed = process_entire_dataset(X_test)#trata as imagens de teste

model_processed = createModel(train_processed, labels_train)#Cria classificador com processamento
acc_train_proc = metrics.accuracy_score(predict(model_processed,train_processed),labels_train)
acc_test_proc = metrics.accuracy_score(predict(model_processed,test_processed),labels_test)

print("Acuracia do treinamento(com preprocessamento): "+ str(acc_train_proc))
print("Acuracia do teste(com preprocessamento): "+ str(acc_test_proc))

