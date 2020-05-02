import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.png')

original = cv2.imread(lena, 0)

kernel = np.ones((5, 5))
dilated = cv2.dilate(original, kernel)
eroded = cv2.erode(original, kernel)
opened = cv2.morphologyEx(original, cv2.MORPH_OPEN, kernel)
closed = cv2.morphologyEx(original, cv2.MORPH_CLOSE, kernel)
top_hat_opening = cv2.morphologyEx(original, cv2.MORPH_TOPHAT, kernel)
top_hat_closing = cv2.morphologyEx(original, cv2.MORPH_BLACKHAT, kernel)

plt.figure('original')
plt.imshow(original, cmap='gray')

plt.figure('dilated')
plt.imshow(dilated, cmap='gray')

plt.figure('eroded')
plt.imshow(eroded, cmap='gray')

plt.figure('opened')
plt.imshow(opened, cmap='gray')

plt.figure('closed')
plt.imshow(closed, cmap='gray')

plt.figure('top hat opening')
plt.imshow(top_hat_opening, cmap='gray')

plt.figure('top hat closing')
plt.imshow(top_hat_closing, cmap='gray')

plt.show()
