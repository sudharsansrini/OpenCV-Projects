import cv2

cam= cv2.VideoCapture(0)
print(cam.get(3))
print(cam.get(4))
while(cam.isOpened()):
    ret, frame = cam.read()
    if ret == True:
        #cam.set(3, 1080)
        #cam.set(4, 640)
        #print(cam.get(3))
        #print(cam.get(4))

        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()


