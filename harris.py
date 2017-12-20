import cv2
import numpy as np

img = cv2.imread('martin_face.jpg')
img = cv2.resize(img,None,fx=.2,fy=.2, interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray,2,3,0.04)

dst = cv2.dilate(dst,None)

img[dst>0.1*dst.max()]=[0,0,255]

cv2.imshow('dst',img)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()
