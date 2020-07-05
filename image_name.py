import cv2
import argparse
import os

c=1

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input images")
ap.add_argument("-o", "--output", required=True, help="path to output images")
ap.add_argument("-n", "--name", required=True, help="nameing convention")
args = vars(ap.parse_args())

inD=args["input"]
oD=args["output"]
name=args["name"]

count=1

for filename in os.listdir(inD):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
        img=cv2.imread(os.path.join(inD, filename))
        cv2.imwrite(oD+name+str(c)+".jpg",img)
        c=c+1
    else:
        continue
