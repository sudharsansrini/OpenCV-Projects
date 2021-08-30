import cv2
import numpy as np

def nothing(x):
    print(x)


cv2.namedWindow('image')
img = np.zeros((512, 512, 3), np.uint8)
switch = "OFF-0 \n ON-1"

#B = img[:, :, 0]
#G = img[:, :, 1]
#R = img[:, :, 2]
cv2.createTrackbar('B', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break


    b = cv2.getTrackbarPos('B', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    r = cv2.getTrackbarPos('R', 'image')
    s = cv2.getTrackbarPos(switch, 'image')



    if s == 0:
       img[:] = 0
    else:
       img[:] = [b, g, r]
       #cv2.imshow('image', img)
cv2.destroyAllWindows()