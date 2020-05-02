import os
import cv2
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.png')

original = cv2.imread(lena, 0)
median_filtering = cv2.medianBlur(original, 5)
# O segundo argumendo é o depth da img destino
# Usando -1, o depth será igual ao da imagem original
avg_filtering = cv2.boxFilter(original, -1, 5)

plt.figure('original')
plt.imshow(original, cmap='gray')

plt.figure('median_filtering')
plt.imshow(median_filtering, cmap='gray')

plt.figure('avg_filtering')
plt.imshow(avg_filtering, cmap='gray')

plt.show()
