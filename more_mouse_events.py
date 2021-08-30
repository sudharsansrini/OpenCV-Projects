import cv2
import numpy as np
def click_events(events, x, y, flag, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 3, (0,0,255), -1)
        point.append((x,y))
        if len(point) >= 2:
            cv2.line(img, point[-1], point[-2], (255, 0, 0), 4)
        cv2.imshow('image', img)

    if events == cv2.EVENT_RBUTTONDOWN:
        blue= img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        my_colour_image= np.zeros((512,512,3), np.uint8)

        my_colour_image[:] = [blue, green, red]
        cv2.imshow('rgb', my_colour_image)


#img = cv2.imread('lena.jpg')
img = np.zeros((512, 512, 3), np.uint8)
point=[]
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()