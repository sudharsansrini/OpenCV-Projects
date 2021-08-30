import cv2
import numpy as np


def click_events(events, x, y, flag, param):
    if events == cv2.EVENT_LBUTTONDOWN:
        print(x, y)
        font = cv2.FONT_HERSHEY_COMPLEX
        strXY = str(x) + ',' + str(y)
        cv2.putText(img, strXY, (x,y), font, 0.5, (255,255,255), 2)
        cv2.imshow('image', img)


img = cv2.imread('traffic.png')
cv2.rectangle(img, (665, 512), (665+70, 512+38), (0, 255, 0), 2)
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_events)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
cap = cv2.VideoCapture('highway1.mp4')
ret, frame = cap.read()
print(frame)
x, y, w, h = 200, 172, 70, 38
track_window = (x, y, w, h)
roi = frame[y:y + h, x:x + w]
#print(roi)

hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
cv2.imshow('roi', roi)

while 1:
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)

        x, y, w, h = track_window
        final_img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('dst', dst)
        cv2.imshow('final', final_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
"""