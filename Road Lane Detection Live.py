import cv2
import numpy as np
import matplotlib.pylab as plt


def region_of_vertices(img, vertices):
    mask = np.zeros_like(img)
    match_mask_color = 255
    # points = cv2.convexHull(region_of_interest_vertices)
    cv2.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), 3)
    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


#image = cv2.imread('road.png')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

def process(image):
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    height = image.shape[0]
    width = image.shape[1]

    region_of_interest_vertices = [(0, height), (width / 2, height / 2), (width, height)]
    print(region_of_interest_vertices)
    Canny_img = cv2.Canny(imgray, 60, 120)
    cropped = region_of_vertices(Canny_img, np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped, 2, np.pi / 60, 106, np.array([]), minLineLength=40, maxLineGap=95)

    image_with_lines = draw_lines(image, lines)
    return image_with_lines

cap = cv2.VideoCapture('data/lane.mp4')
# cap = cv2.VideoCapture('data/lane1.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    frame = process(frame)
    #plt.imshow(image_with_lines)
    #plt.show()
    cv2.imshow('detected', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
