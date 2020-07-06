import os

image_files = []
os.chdir("dataset")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".jpg"):
        image_files.append("dataset/" + filename)
os.chdir("..")
with open("train.txt", "w") as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()