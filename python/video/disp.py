import numpy as np
import cv2

cap = cv2.VideoCapture(0)

Skip = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (7,7), 0)
    edge = cv2.Canny(blur, 20, 100)

    # Display the resulting frame
    Skip = Skip + 1 

    if Skip % 5 == 0:
        cv2.imshow('frame',edge)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()