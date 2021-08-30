import cv2
import numpy as np

#print(img.size)
#print(img.shape)
#print(img.dtype)
def click_events(events, x,y , flag, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        font= cv2.FONT_HERSHEY_COMPLEX
        wid_hei = (str(x) + ',' + str(y))
        cv2.putText(img, wid_hei, (x,y) ,font, 0.2, (0,0,0), 1)
        cv2.imshow('image', img)
#b, g, r = cv2.split(img)
#print(b, g, r)
#cv2.merge((b,g,r))


img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img= cv2.resize(img,(512,512))
img2= cv2.resize(img2,(512,512))
#dst=cv2.add(img,img2)
#dst=cv2.addWeighted(img,0.8,img2,0.2,0)
cv2.imshow('image', img)
#cv2.imshow('image', dst)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()
