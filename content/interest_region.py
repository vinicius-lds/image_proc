import os
import cv2
from matplotlib import pyplot as plt


lena = os.path.join('input_data', 'lena.png')

original = cv2.imread(lena)

r = cv2.selectROI(original)
cv2.destroyAllWindows()

crop = original[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

plt.figure('original')
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))

plt.figure('crop')
plt.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))

plt.show()