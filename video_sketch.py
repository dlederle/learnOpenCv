import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    #sketch_gray, sketch_color = cv2.pencilSketch(frame, sigma_s=10, sigma_r=0.15, shade_factor=0.05)
    #display = sketch_color
    #display = cv2.stylization(frame, sigma_s=60, sigma_r=0.07)
    display = cv2.detailEnhance(frame, sigma_s=10, sigma_r=0.15)


    cv2.imshow('frame', display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
