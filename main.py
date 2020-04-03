import sys
sys.path.append('./functions')

from image_processing import *


(X_train, labels_train), (X_test, labels_test) = load_dataset('./data')
print('Dataset obtido')
print('Processando dataset...')
dataset_train_processed = process_entire_dataset(X_train)
dataset_test_processed = process_entire_dataset(X_test)

# Incrementar classificador e resultados ao final
