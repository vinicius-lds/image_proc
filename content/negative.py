import os
import cv2
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.png')

original = cv2.imread(lena, 0)
negative = 255 - original

plt.figure(1)
plt.imshow(original, cmap='gray')

plt.figure(2)
plt.imshow(negative, cmap='gray')

plt.show()
