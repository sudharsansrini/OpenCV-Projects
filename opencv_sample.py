import cv2

# READ
img = cv2.imread('lena.jpg', 1)
print(img)

# SHOW
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# WRITE
# cv2.imwrite('lena_copy.png', img)