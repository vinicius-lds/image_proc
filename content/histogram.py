import os
import cv2
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.jpg')

# path da imagem e o 0 indica que será lida em grayscale
img = cv2.imread(lena, 0)

# cmap = color map
plt.imshow(img, cmap='gray') 
plt.show()

# img.ravel() tranforma a matriz em um vetor
# bins indica a quantidade de linhas mostradas no grafico
# range é o range de pontos possiveis
plt.hist(img.ravel(), bins=256, range=(0.0, 255.0))
plt.show()
