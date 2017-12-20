import numpy as np
import cv2

img = cv2.imread('martin_face.jpg')
img = cv2.resize(img,None,fx=.2,fy=.2, interpolation = cv2.INTER_CUBIC)
dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=10, sigma_r=0.15, shade_factor=0.05)

cv2.imshow('image', dst_color)

k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
