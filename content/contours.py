import os
import cv2
from matplotlib import pyplot as plt


lena = os.path.join('input_data', 'forms.png')

original = cv2.imread(lena, 0)
_, threshold = cv2.threshold(original, 220, 255, cv2.THRESH_BINARY)


plt.figure('original')
plt.imshow(original, cmap='gray')

plt.figure('binary')
plt.imshow(threshold, cmap='gray')

plt.show()

contours = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
print(contours)
cv2.drawContours(original, contours, -1, (255, 0, 0), 3)

plt.figure('contours')
plt.imshow(original, cmap='gray')

plt.show()