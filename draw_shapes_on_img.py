import cv2

img = cv2.imread('lena.jpg')
#img = cv2.line(img, (0,0), (255, 255), (255, 0, 0), 5)
#img = cv2.circle(img, (100, 100) , 50, (0,255,255), -1)
#img = cv2.rectangle(img, (0,100), (200, 0), (0, 255, 0), -1)
#img= cv2.arrowedLine(img,(0,0),(255,255), (255, 0, 0), 5 )
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Hi Lena!', (0,255), font, 4, (0, 0, 255), 2, cv2.LINE_AA)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()