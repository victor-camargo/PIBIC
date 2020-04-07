import sys
sys.path.append('./functions')

from image_processing import *
import cProfile
import matplotlib.pyplot as plt

(X_train, labels_train), (X_test, labels_test) = load_dataset('./data')
print('Dataset obtido')
print('Processando dataset...')


dataset_train_processed = process_entire_dataset(X_train)
dataset_test_processed = process_entire_dataset(X_test)

#cProfile.run('to_analyze()')
plt.imshow(image_preprocessing(dataset_train_processed[0].reshape(28,28)), cmap='gray')
plt.show()
# Incrementar classificador e resultados ao final
