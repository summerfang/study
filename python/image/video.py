import cv2
cap = cv2.VideoCapture('/dev/video0')
success, frame = cap.read()
height, width = 720, 1280
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cap.set(cv2.CAP_PROP_FPS, 60)

while True:
    success, frame = cap.read()

cv2.imwrite("test.jpg", frame)