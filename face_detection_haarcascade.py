import cv2
import numpy as np

face_cascade =cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture('data/megamind.avi')
# cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, image = cap.read()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)

    cv2.imshow('video', image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()