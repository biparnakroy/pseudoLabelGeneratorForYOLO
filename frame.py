import cv2
import numpy as np
import math
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True, help="path to input video")
ap.add_argument("-d", "--dir", required=True, help="path to output frames")
ap.add_argument("-n", "--name", required=True, help="nameing convention")
ap.add_argument("-i", "--interval", required=True, help="interval of frame slicing in seconds")
args = vars(ap.parse_args())

name=args["name"]
dir=args["dir"]
cap= cv2.VideoCapture(args["video"])
frameRate = cap.get(5) #frame rate
x=1
while True:
    frameId = cap.get(1)
    _, frame =cap.read()
    #uncomment if you want to rotate the frames
    #frame=cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    if (frameId % (math.floor(frameRate)*int(args["interval"])) == 0):
        filename = dir +name+ str(int(x)) + ".jpg";x+=1
        cv2.imwrite(filename, frame)
cap.release()
print ("Done!")

