import sys
sys.path.append('./functions')

from deskew import *
from mnist_funcs import *
from thinning import *
import matplotlib.pyplot as plt


(X_train, labels_train), (X_test, labels_test) = load_dataset()

for img in X_train:
    
    img = img.reshape(28,28).astype(np.uint8) #Transforma vetor em uma imagem 28x28

    plt.subplot(1,4,1)
    plt.title("Original")
    plt.imshow(img, cmap='gray')
    
    plt.subplot(1,4,2)
    plt.title("Deskewed")
    desk = deskew(img) #Realiza a compensação dos digitos
    desk = cv2.normalize(desk, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1) #Normaliza a imagem para aplicar Otsu
    plt.imshow(desk, cmap='gray')

    plt.subplot(1,4,3)
    plt.title("Otsu Threshold")
    ret, thresh = cv2.threshold(desk, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # limiariza usando Otsu
    plt.imshow(thresh, cmap='gray')

    plt.subplot(1,4,4)
    plt.title("Zhang Suen\nSkeletonization")
    #skel, distance =  medial_axis(thresh, return_distance=True)
    #plt.imshow(skel*distance, cmap='gray')
    skel= zhangSuen(thresh) # Aplica a esqueletonização rapida de Zhang-Suen
    plt.imshow(skel, cmap='gray')
    
    plt.show()
