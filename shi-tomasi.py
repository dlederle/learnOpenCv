import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('martin_face.jpg')
img = cv2.resize(img,None,fx=.2,fy=.2, interpolation = cv2.INTER_CUBIC)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray,5,0.01,10)
corners = np.int0(corners)


for i in corners:
    x,y = i.ravel()
    cv2.circle(img, (x,y),3,255,-1)

plt.imshow(img),plt.show()
