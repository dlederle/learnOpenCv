import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('martin_face.jpg', 0)

#Shrink the image and grab some dimensions
img = cv2.resize(img,None,fx=.2,fy=.2, interpolation = cv2.INTER_CUBIC)
rows,cols = img.shape

pts1 = np.float32([[50,50], [200,50],[50,200]])
pts2 = np.float32([[10,100], [200,50],[150,250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img),plt.title("input")
plt.subplot(122),plt.imshow(dst),plt.title("output")
plt.show()

#k = cv2.waitKey(0)
#if k == ord('q'):
#    cv2.destroyAllWindows()
