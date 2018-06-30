import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
while(True):

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, 0)
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()