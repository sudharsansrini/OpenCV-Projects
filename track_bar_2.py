import cv2
import numpy as np


def nothing(x):
    print(x)


switch = "COLOR/GRAY"
cv2.namedWindow('image')
cv2.createTrackbar('CP', 'image', 0, 100, nothing)
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    img = cv2.imread('lena.jpg')

    cv2.imshow('image', img)

    pos = cv2.getTrackbarPos('CP', 'image')
    #print("p")
    font = cv2.FONT_HERSHEY_COMPLEX
    img= cv2.putText(img, str(pos), (50, 100), font, 3, (0, 255, 0), 1)

    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

    s = cv2.getTrackbarPos(switch, 'image')
    #print("s")
    if s == 0:
        pass
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.destroyAllWindows()
