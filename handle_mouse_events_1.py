import cv2
import numpy as np
def click_events(events, x, y, flag, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,255), 2)
        cv2.imshow('image', img)

    if events == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_COMPLEX
        strBGR = str(blue) + ',' + str(green) + ',' + str(red)
        cv2.putText(img, strBGR, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('image', img)

img = np.zeros((512,512,3), np.uint8)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()