import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Gradient.png', 0)

_,th1 = cv2.threshold(img, 120, 100, cv2.THRESH_BINARY)
_, th2 = cv2.threshold(img, 120, 100, cv2.THRESH_BINARY_INV)
_, th3= cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, th4= cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, th5= cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles=['Th1', 'Th2', 'Th3', 'th4', 'th5']
images=[th1, th2, th3, th4, th5]

for i in range(5):
    plt.subplot(2,3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])
plt.show()