import cv2
import numpy as np
from PIL import Image
import pytesseract as py
py.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('data/ocr.jpg')
# img = cv2.imread('data/ocr2.jpg')
cv2.imshow('image', img)

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(imgray, 5)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

print(py.image_to_string(thresh, lang='eng'))

cv2.waitKey(0)
cv2.destroyAllWindows()
