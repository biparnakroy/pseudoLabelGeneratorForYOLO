import cv2
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-t", "--text", required=True, help="path to input label")
ap.add_argument("-c", "--classes", required=True, help="list of classes")
args = vars(ap.parse_args())

classes = []
with open(args["classes"], "r") as x:
    classes = [line.strip() for line in x.readlines()]

filename = args["text"]
img = cv2.imread(args["image"])

height=int(img.shape[0])
width = int(img.shape[1])



with open(filename) as f:
    content = f.readlines()

content = [x.strip() for x in content] 

if len(content)>0:
    for i in content:
        if (int(i.split()[5]) > 0 and int(i.split()[3]) > 0):
            l=""
            for c in classes:    
                l=l+str(classes.index(i.split()[0][:len(i.split()[0])-1]))

            Ax=int(i.split()[3])+(int(i.split()[7])/2)
            x= int(Ax)/width
            l=l+str("%.6f"%x)+" "
            
            Ay=int(i.split()[5])+(int(i.split()[9][:len(i.split()[9])-1])/2)
            y= int(Ay)/height
            l=l+str("%.6f"%y)+" "

            w= int(i.split()[7])/width
            l=l+str("%.6f"%w)+" "
        
            h= int(i.split()[9][:len(i.split()[9])-1])/height
            l=l+str("%.6f"%h)

            print(l)
