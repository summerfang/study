import cv2
import sys

image = cv2.imread(sys.argv[1])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(gray_image, (7,7), 0)
cv2.imshow("Original Image", image)
canny = cv2.Canny(blur_image, 10, 30)
cv2.imshow("Canny with low thresholds", canny)
canny2 = cv2.Canny(blur_image, 50, 150)
cv2.imshow("Canny with high thresholds", canny2)
cv2.waitKey(0)