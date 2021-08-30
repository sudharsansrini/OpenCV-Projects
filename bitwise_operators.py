import cv2
import numpy as np
img1 = np.zeros((512, 512, 3), np.uint8)
img1 = cv2.rectangle(img1, (200,0), (300,100), (255,255,255), -1)
img2= cv2.imread('image_1.jpg')
img2 = cv2.resize(img2, (512,512))
cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
bit_and= cv2.bitwise_and(img2,img1)
bit_or= cv2.bitwise_or(img2,img1)
bit_xor= cv2.bitwise_xor(img2,img1)
bit_not1= cv2.bitwise_not(img1)
bit_not2= cv2.bitwise_not(img2)


cv2.imshow('and', bit_and)
cv2.imshow('or', bit_or)
cv2.imshow('xor', bit_xor)
cv2.imshow('not1', bit_not1)
cv2.imshow('not2', bit_not2)
cv2.waitKey(0)
cv2.destroyAllWindows()