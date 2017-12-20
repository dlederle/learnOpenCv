#http://www.computervisiononline.com/blog/tutorial-using-camshift-track-objects-video
import numpy as np
import argparse
import cv2

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video",
            help = "Path to the (original) video file")
    args = vars(ap.parse_args())

    if not args.get("video", False):
        camera = cv2.VideoCapture(0)
    else:
        camera = cv2.VideoCapture(args["video"])

    cv2.namedWindow("frame")
    hog = cv2.HOGDescriptor()

    while True:
        (grabbed, frame) = camera.read()

        if not grabbed:
            break


        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

