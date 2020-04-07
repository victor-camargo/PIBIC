#from deskew_c import *
from deskew import *
from mnist_funcs import *
from thinning import *
from skimage.filters import threshold_otsu
from skimage.morphology import skeletonize
import numpy as np
import cv2

def image_preprocessing(image):
    
    #img = image.reshape(28,28) #Transforma vetor em uma imagem 28x28
    desk = deskew(image.reshape(28,28)) #Realiza a compensação dos digitos
    ret, thresh = cv2.threshold(desk, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) # limiariza usando Otsu  
    return skeletonize(thresh.astype(np.bool))

def process_entire_dataset(data):
    
    processed = []
    for i in range(len(data)):
        processed.append(image_preprocessing(data[i]).flatten())
    return np.array(processed)
