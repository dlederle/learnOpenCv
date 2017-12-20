import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

img = cv2.line(img,(0,0),(511,511),(255,0,0),5)

img = cv2.rectangle(img, (385, 0), (510, 128), (0,255,0),3)


cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == ord('q'):
    cv2.destroyAllWindows()
