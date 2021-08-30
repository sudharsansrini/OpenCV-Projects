import cv2
import numpy as np

img= cv2.imread('sudoku.png',)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(img, 50, 150, apertureSize=3)
cv2.imshow("edegs", edge)
lines = cv2.HoughLines(edge, 1, np.pi/180, 225)

for line in lines:
    rho, theta = line[0]
    a=np.cos(theta)
    b= np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()