import cv2
import numpy as np

cap = cv2.VideoCapture('data/vtest.avi')
# 1 fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
# 2 fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows = False)
# 3 fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN()
while cap.isOpened():
    ret, frame = cap.read()
    fg_mask = fgbg.apply(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('FG_MASK_frame', fg_mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()