import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.cvtColor(cv2.imread('imgHist.png'), cv2.COLOR_BGR2RGB)

expanded = cv2.convertScaleAbs(original, beta=25, alpha=9)
median_filtering = cv2.medianBlur(expanded, 11)
avg_filtering = cv2.boxFilter(median_filtering, -1, (11, 11))

plt.figure(1)
plt.imshow(original)

plt.figure(2)
plt.hist(original.ravel(), bins=256, range=(0.0, 255.0))

plt.figure(3)
plt.imshow(avg_filtering)

plt.figure(4)
plt.hist(avg_filtering.ravel(), bins=256, range=(0.0, 255.0))

plt.show()
