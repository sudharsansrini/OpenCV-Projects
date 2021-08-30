import cv2

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output= cv2.VideoWriter('output.mp4', fourcc, 20.0, (4,4))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        print(cv2.CAP_PROP_FRAME_WIDTH)
        print(cv2.CAP_PROP_FRAME_HEIGHT)
        output.write(gray)
        cv2.imshow('video', gray)
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break


capture.release()
output.release()
cv2.destroyAllWindows()
