#http://www.computervisiononline.com/blog/tutorial-using-camshift-track-objects-video
import numpy as np
import argparse
import cv2

def find_marker(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5,5),0)
    edged = cv2.Canny(gray, 35, 125)

    (cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    c = max(cnts, key=cv2.contourArea)

    return cv2.minAreaRect(c)

def distnace_to_camera(knownWidth, focalLength, perWidth):
    return (knownWidth * focalLength) / perWidth

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image",
            help = "Path to the (original) image file")
    args = vars(ap.parse_args())



    if not args.get("image", False):
        img = cv2.imread("martin_face.jpg")
        img = cv2.resize(img,None,fx=.2,fy=.2,interpolation = cv2.INTER_CUBIC)
    else:
        img = cv2.imread(args["image"])

    cv2.namedWindow("frame")
    cv2.imshow("frame", img)

    key = cv2.waitKey(0) & 0xFF
    if key == ord("q"):
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

