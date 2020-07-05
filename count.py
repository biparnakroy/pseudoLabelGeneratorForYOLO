import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--start", required=True, help="staring point of the label")
ap.add_argument("-e", "--end", required=True, help="path to input label")
args = vars(ap.parse_args())

start = args["start"]
end = args["end"]
s=""
for i in range(int(start),(int(end)+1)):
    s=s+str(i)+" "
print(s)
