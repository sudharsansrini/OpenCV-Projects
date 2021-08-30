import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE)
_, mask = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY_INV)
kernal = np.array((3, 3), np.uint8)

dilation = cv2.dilate(mask, kernal, iterations=2)
erosion = cv2.erode(mask, kernal, iterations=1)  # size reduce
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)  # 1.erosion 2. dilation
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)  # 1.dilation 2.erosion
gradient = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)  # dilation - erosion
tophat = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)  # mask - opening

titles = ['Mask', 'Dilation', 'Erosion', 'Opening', 'Closing', 'Gradient', 'tophat']
images = [mask, dilation, erosion, opening, closing, gradient, tophat]

for i in range(7):
    plt.subplot(3, 4, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

# cv2.imshow('image', img)
# cv2.imshow('mask', mask)
# cv2.imshow('image3', kernal)
# cv2.imshow('dilation', dilation)
# cv2.imshow('erosion', erosion)
# cv2.imshow('opening', opening)
# cv2.imshow('closing', closing)
# cv2.imshow('gradient', gradient)
# cv2.imshow('tophat', tophat)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
