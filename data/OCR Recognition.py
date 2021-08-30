import cv2
import numpy as np
from PIL import Image
import pytesseract as py

"""
def oct_to_string(image):
    text = py.image_to_string(image)
    return text
"""

img = cv2.imread('ocr.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(imgray, 5)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

print(py.image_to_string(thresh, lang='eng'))
