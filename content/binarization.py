import os 
import cv2
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.png')

original = cv2.imread(lena, 0)
_, binary = cv2.threshold(original, 120, 255, cv2.THRESH_BINARY)

plt.figure(1)
plt.imshow(original, cmap='gray')

plt.figure(2)
plt.imshow(binary, cmap='gray')

plt.show()
