import numpy as np
import cv2

cap = cv2.VideoCapture('output.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('p'):
            paused = True
            while(paused):
                if cv2.waitKey(1) & 0xFF == ord('c'):
                    paused = False
    else:
        break

cap.release()
cv2.destroyAllWindows()
