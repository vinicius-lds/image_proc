import os

import cv2
from matplotlib import pyplot as plt

lena = os.path.join('input_data', 'lena.png')

# Deve ser feita a converção de BGR para RGB, isso porque o opencv
# le imagens em BGR
original = cv2.cvtColor(cv2.imread(lena), cv2.COLOR_BGR2RGB)

plt.figure('original')
plt.imshow(original)

r, g, b = cv2.split(original)

plt.figure('red')
plt.imshow(r, cmap='Reds')

plt.figure('green')
plt.imshow(g, cmap='Greens')

plt.figure('blue')
plt.imshow(b, cmap='Blues')

merged_rgb = cv2.merge((r, g, b))

plt.figure('merged rgb')
plt.imshow(merged_rgb)

plt.show()

hsv = cv2.cvtColor(original, cv2.COLOR_RGB2HSV)

plt.figure('hsv')
plt.imshow(hsv)

h, s, v = cv2.split(hsv)

plt.figure('h')
plt.imshow(h)

plt.figure('s')
plt.imshow(s)

plt.figure('v')
plt.imshow(v)

merged_hsv = cv2.merge((h, s, v))

plt.figure('merged hsv')
plt.imshow(merged_hsv)

plt.show()
