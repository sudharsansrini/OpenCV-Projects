import cv2
import numpy as np

img= cv2.imread('messi5.jpg')
imgray =  cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template= cv2.imread('messi-face.jpg',0)

w, h = template.shape[::-1]  # template.shape gives (h,w). By reversing we get w, h

res = cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)
#print(res)
threshold=0.95

loc = np.where(res>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 255, 0), 1)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()