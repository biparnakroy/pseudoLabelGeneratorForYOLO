# artificialYOLOtrainer

Clone the entire repository with the Darknet submodule by executing the following command:

``` 
git clone --recurse-submodules https://github.com/biparnakroy/artificialYOLOtrainer.git
```

If you already have the darknet built in your system then ommit ```--recurse-submodules```  and put your ```darknet```  directory inside the ```artificialYOLOtrainer``` directory

## Dependencies

### OS Enviornment

**artificalYOLOtrainer** has native support for *linux OS (ubuntu 20.04) with python 3.8.2* 

### Libraries

There are some library dependencies : opencv-python, numpy, math, argparse, imutils, requests. 

You can install these libraries by executing the following command **(recomended)**

```
pip install -r requirements.txt
```
else you can also use:
```
pip install opencv-python
pip install numpy
pip install math
pip install argparse
```

## Building Darknet

If you already have darknet built in your system _(which is mostlikey the case because the main use of **artficialYOLOtrainer** to generate datasets using pretrained YOLO weights for further training of the model)_ then the following steps are not required.

**Note**: Make sure you have your ```darknet``` (prebuilt) directory inside the ```artificialYOLOtrainer``` directory.

However if dont't have darknet built in your system then ```cd in to the darknet directory``` and build darknet following [AlexyAB's guide](https://github.com/AlexeyAB/darknet/tree/3af6781de273fa01f4a535c8e40c5056e809e22f)

 Now we have to set up ```obj.names``` and ```obj.data``` files in ```data``` directory inside ```darknet```

 *obj.names:*
 The obj.names should contain the following:

 ```
 <class1>
 <class2>
  ....

 ```
 *obj.data:*
 The obj.data should cotain the following:
 ```
    classes= <number of classes>
    train  = data/train.txt
    valid = data/test.txt
    names = data/obj.names
    backup = ../new_weights
```
The ```train.txt``` and ```text.txt``` contains the the paths of images for training and test respectively.They will be configured when we are done generating the labels for our dataset and ready to retrain the model.

The ```backup= ../new_weights``` is basically to store the checkpoints of the weights generated on further traing. At this stage the new_weights directory should be empty. **(even if you have darknet prebuilt then set the backup path to ../new_weights)**


## Configuring pretrained weights and cfg files

Put the pretrained yolo weights inside ```weights``` directory and yolo config files in ```cfg``` directory.

## Gathering images for the new Dataset
The particular use case suggests that we create a custom dataset. This can be done by either mass dowloading images from internet or by slicing frames from video files.

### Code to mass download images from Google Images using JavaScript Console Window and python script.
This guide is based on [The AI Guys's tutorial](https://github.com/theAIGuysCode/Download-Google-Images)

Steps to perform:
- Query your intended Google search
- Scroll down through images until they become unrelated to your query or until you've passed enough images for your dataset
- Right click and hit "Inspect" and then navigate to "Console" tab
- One by one enter the lines from ```console.js``` into the console window and run them
- Move ```urls.txt``` containing the urls of the images from ```Downloads``` directory to ```artificialYOLOtrainer``` directory
- The images will be downloaded in ```images``` directory
- Run follwing python command as follows:
```
python3 download_imgs.py --urls urls.txt --output images
```

You should now have all your images inside your images folder!

#### Now we have to format the names of images following this convention 
```<name of dataset>serial no.>.jpg```

Run the follwing python command to do so.

```
 python3 image_name.py --input images/ --output dataset/ --name data
```
In place ```--name data``` pass the name of your own dataset, and be use it in place of ```data``` further on.
After this you can see that the ```dataset``` directory will have images named as ```data1.jpg, data2.jpg ......```


### Code to slice frames from video file.
Run the follwing python command to do so.

```
 python3 frame.py --input <video file> --output dataset/ --interval <int> --name data 
```
Here ```--interval``` is the interval of frame slicing in seconds , ```--name``` flag is used for the naming convention
After this we will see ```dataset``` directory has images named as ```data1.jpg, data2.jpg ......```

# Running Pretrained YOLO model on The new dataset
Now we have to run trained YOLO model to produce the labels of the new dataset that was created in ```dataset``` directory.
-   Generating the number list corresponding to the number of images in dataset
 Run the following python command to generate number list

```python3 count.py --start <staring serial no.> --end <ending serial number>
```
Here the <starting serial no.>  is the number corresponding to the ```data1.jpg``` and  <ending serial no.> that serial no. of last image in dataset.

This is will generate a output like this
```
1 2 3 4 5 6 . . . . . .
```
copy this list.

- Configing darknet.sh
Open ```darknet.sh```
```
cd darknet
for i in   <num list>
do
  ./darknet detector test  data/obj.data  ../cfg/<cfg file>                ../weights/<weight file>                -ext_output -dont_show   ../dataset/data$i.jpg  > ../dataset/data$i.txt
done
```
Here is place of ```<num list>``` paste the list of numbers generated from ```count.py```, in place of ```<cfg file>``` put the name of the config file which is place in ```cfg``` directory, in place of ```<weight file``` put the name of the pretrained YOLO weights placed inside ```weights``` directory.

Now run the following commands (inside the parent directory):

```
chmod +x darknet.sh
./darknet.sh
```

