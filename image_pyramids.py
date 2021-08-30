import cv2
import numpy as ap

img = cv2.imread('lena.jpg')

layer = img.copy()
gp =[layer]

# Gaussian_Pyramid
for i in range(6):
    layer = cv2.pyrDown(layer)
    gp.append(layer)
    # cv2.imshow(str(i), gp[i])

# Laplacian pyramid
layer1= gp[5]
lp= [layer1]

for j in range(5, 0, -1):
    Gaussian_extended = cv2.pyrUp(gp[j])
    laplacian = cv2.subtract(gp[j-1], Gaussian_extended)
    cv2.imshow(str(j), laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()