import cv2
import sys

image = cv2.imread(sys.argv[1])
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.GaussianBlur(image, (7,7), 0)

cv2.imshow("Original Image", image)
cv2.imshow("Gray Image", gray_image)
cv2.imshow("Blur Image", blur_image)

cv2.waitKey(0)