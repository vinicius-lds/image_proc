import cv2
import numpy as np
from matplotlib import pyplot as plt



def process(img):
    gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    negative = 255 - gray_scale
    sei_la = negative + 50
    _, binary = cv2.threshold(negative, 170, 255, cv2.THRESH_BINARY)    
    sl = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, np.ones((30, 30)))

    plt.figure(1)
    plt.imshow(sl, cmap='gray')

    plt.show()
    

chuvoso = cv2.imread('chuvoso.png')
estiagem = cv2.imread('estiagem.png')

process(chuvoso)
# process(estiagem)



