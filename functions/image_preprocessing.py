from deskew import *
from mnist_funcs import *
from thinning import *


def image_preprocessing(image):
    
    #img = image.reshape(28,28) #Transforma vetor em uma imagem 28x28
    desk = deskew(image) #Realiza a compensação dos digitos
    desk = cv2.normalize(desk, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1) #Normaliza a imagem para aplicar Otsu
    ret, thresh = cv2.threshold(desk, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # limiariza usando Otsu
    skel= zhangSuen(thresh) # Aplica a esqueletonização rapida de Zhang-Suen
    return skel

def process_entire_dataset(data):
    processed = []
    for i in range(len(data)):
        processed.append(image_preprocessing(data[i].reshape(28,28)).flatten())
    return np.array(processed)
