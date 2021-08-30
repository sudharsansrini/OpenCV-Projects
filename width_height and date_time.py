import cv2
import datetime
cam= cv2.VideoCapture(0)
#print(cam.get(3))
#print(cam.get(4))
while(cam.isOpened()):
    ret, frame = cam.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_COMPLEX
        WB = 'Width :' + str(cam.get(3)) + ',' + 'Height :' + str(cam.get(4))
        DT = str(datetime.datetime.now())
        #print(DT)
        #print(WB)
        frame = cv2.putText(frame, WB , (10, 50), font, 1, (0,0,0),  1, cv2.LINE_AA)
        frame = cv2.putText(frame, DT, (0, 450), font, 1, (0, 0, 0), 1, cv2.LINE_AA)
        cv2.imshow('video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()
cv2.destroyAllWindows()


