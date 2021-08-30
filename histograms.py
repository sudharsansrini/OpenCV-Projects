import cv2
import numpy as np
from matplotlib import pyplot as plt

# BLACK IMAGE HIST
"""
black = np.zeros((200, 200), np.uint8)
cv2.imshow('black', black)
plt.hist(black.ravel(), 256, [0, 256])
plt.show()

"""
# WHITE & GRAY IMAGE HIST
"""
black = np.zeros((200, 200), np.uint8)
cv2.rectangle(black, (0, 100), (200, 200), (255, 255, 255), -1)
cv2.rectangle(black, (0, 50), (100, 100), (127), -1)
cv2.imshow('black', black)
plt.hist(black.ravel(), 256, [0, 256])
plt.show()
"""

# GRAY IMAGE
"""
img= cv2.imread('lena.jpg', 0)
plt.hist(img.ravel(), 256, [0, 256])
plt.show()
"""

# COLOR IMAGE

img= cv2.imread('lena.jpg')
b, g, r = cv2.split(img)
plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])
plt.show()


# USING CALHIST() METHOD
"""
img= cv2.imread('lena.jpg', 0)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()
"""
