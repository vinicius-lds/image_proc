import os
import cv2
import numpy as np


def show(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread(os.path.join('input_data', 'brightness.jpg'))
show(img)
