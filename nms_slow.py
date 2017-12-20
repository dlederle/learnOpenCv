from nms import non_max_suppression_slow
import numpy as np
import cv2

images = [
        ("audrey.jpg", np.array([
            (12, 84, 140, 212),
            (24, 84, 152, 212),
            (36, 84, 164, 212),
            (12, 96, 140, 224),
            (24, 96, 152, 224),
            (24, 108, 152, 236)])),
        ("bksomels.jpg", np.array([
            (114, 60, 178, 124),
            (120, 60, 184, 124),
            (114, 66, 178, 130)])),
        ("gpripe.jpg", np.array([
            (12, 30, 76, 94),
            (12, 36, 76, 100),
            (72, 36, 200, 164),
            (84, 48, 212, 176)]))]

for (imagePath, boundingBoxes) in images:
    print "[x] %d initial bounding boxes" % (len(boundingBoxes))
    image = cv2.imread(imagePath)
    orig = image.copy()

    for(startX, startY, endX, endY) in boundingBoxes:
        cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 0, 255), 2)

    pick = non_max_suppression_slow(boundingBoxes, 0.3)
    print "[x] after applying non-maximum, %d bounding boxes" % (len(pick))

    for(startX, startY, endX, endY) in pick:
        cv2.rectangle(image, (startX, startY), (endX, endY), (0, 255, 0), 2)

    cv2.imshow("oroginal", orig)
    cv2.imshow("after NMS", image)
    cv2.waitKey(0)
