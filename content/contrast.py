import os

import cv2
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.png')

original = cv2.imread(lena, 0)
expanded = cv2.convertScaleAbs(original, alpha=1.5)
compressed = cv2.convertScaleAbs(original, alpha=0.5)

plt.figure('original')
plt.imshow(original, cmap='gray')

plt.figure('hist original')
plt.hist(original.ravel(), bins=256, range=(0.0, 255.0))

plt.figure('hist expanded')
plt.hist(expanded.ravel(), bins=256, range=(0.0, 255.0))

plt.figure('expanded')
plt.imshow(expanded, cmap='gray')

plt.figure('compressed')
plt.imshow(compressed, cmap='gray')

plt.figure('hist compressed')
plt.hist(compressed.ravel(), bins=256, range=(0.0, 255.0))

plt.show()
