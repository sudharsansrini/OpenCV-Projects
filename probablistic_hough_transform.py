import cv2
import numpy as np

img = cv2.imread('sudoku.png')
#img = cv2.imread('')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 50, 150, apertureSize=3)
cv2.imshow('edges', edges)

lines= cv2.HoughLinesP(edges, 1, np.pi/180, 100, maxLineGap=10, minLineLength=100)

for i in lines:
    x1, y1, x2, y2 = i[0]
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('image', img)
k= cv2.waitKey(0)
cv2.destroyAllWindows()