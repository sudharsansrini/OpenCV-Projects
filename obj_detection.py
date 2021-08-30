import cv2
import numpy as np
def nothing(x):
    pass
cap= cv2.VideoCapture(0)  #change -1
cv2.namedWindow('image')
cv2.createTrackbar('LH', 'image', 0, 255, nothing)
cv2.createTrackbar('LS', 'image', 0, 255, nothing)
cv2.createTrackbar('LV', 'image', 0, 255, nothing)
cv2.createTrackbar('UH', 'image', 0, 255, nothing)
cv2.createTrackbar('US', 'image', 0, 255, nothing)
cv2.createTrackbar('UV', 'image', 0, 255, nothing)

while True:
    #frame= cv2.imread('smarties.png')
    _, frame = cap.read()  #change -2
    hsv= cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos('LH', 'image')
    l_s = cv2.getTrackbarPos('LS', 'image')
    l_v = cv2.getTrackbarPos('LV', 'image')
    u_h = cv2.getTrackbarPos('UH', 'image')
    u_s = cv2.getTrackbarPos('US', 'image')
    u_v = cv2.getTrackbarPos('UV', 'image')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)
    res= cv2.bitwise_and(frame, frame, mask=mask)
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cap.release()  #change -3
cv2.destroyAllWindows()