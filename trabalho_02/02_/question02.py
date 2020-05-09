import cv2
import numpy as np
from matplotlib import pyplot as plt



def process(img):
    gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    negative = 255 - gray_scale
    pls50 = negative + 50
    _, binary = cv2.threshold(pls50, 170, 255, cv2.THRESH_BINARY)    
    top_hat = cv2.morphologyEx(binary, cv2.MORPH_TOPHAT, np.ones((30, 30)))

    plt.figure(1)
    plt.imshow(top_hat, cmap='gray')

    plt.show()
    

chuvoso = cv2.imread('chuvoso.png')
estiagem = cv2.imread('estiagem.png')

process(chuvoso)
# process(estiagem)



