## Welcome

Thanks for coming to the page. Be sure to check out info on the [March 2018 Lancaster AI meetup](http://lancasterai.com/2018/03/28/thats-a-wrap-march-2018-meetup/) for more info about this code and a video.

Read more about YOLO (in darknet) and download weight files [here](http://pjreddie.com/darknet/yolo/).

## Dependencies

You will need to install Python3, OpenCV 3.3 or higher, natsort, pickle and any missing libraries I forgot. I'd HIGHLY recommend having CUDA 9.0+, cuDNN 7+ installed as well.

PLEASE NOTE: I am using Python3 in a [virtual environment](https://virtualenv.pypa.io/en/latest/installation/), which is why I can use the 'python blah' command to run my code versus 'python3 blah'. If you run into problems running the 'python' commands in these examples, try using 'python3' in its place or learn to use a virtualenv, which is the better way.

This is not a small task. Getting all of these installed and working correctly can take a whole night of your life, so plan accordingly. You CAN just use them without the CUDA and cuDNN, which will shave a bunch of time (and save your lifeforce). Just remember the performance won't be great, and [PyTorch](https://github.com/marvis/pytorch-yolo2) and [Darknet](https://pjreddie.com/darknet/yolov2/) original versions give you the best FPS.


### Getting started

Install the frameworks you want to work with. Here is the listing again:

Darknet (Original) [https://pjreddie.com/darknet/yolov2/](https://pjreddie.com/darknet/yolov2/)
AlexeyAB (Windows/Linux): [https://github.com/AlexeyAB/darknet ](https://github.com/AlexeyAB/darknet)
PyYolo - Python Wrapper on C [https://github.com/digitalbrain79/pyyolo ](https://github.com/digitalbrain79/pyyolo)
Darkflow - Tensorflow [https://github.com/thtrieu/darkflow ](https://github.com/thtrieu/darkflow)
PyTorch-Yolo2 - [https://github.com/marvis/pytorch-yolo2](https://github.com/marvis/pytorch-yolo2)  + many more
Caffee-Yolo - Outdated :( - [https://github.com/yeahkun/caffe-yolo](https://github.com/yeahkun/caffe-yolo)

Place the stuff in right folders, i.e. backup goes into backup. If the folder doesn't exist, just create it. This is based on the original [darkflow](https://pjreddie.com/darknet/yolov2) filesystem.  

You should be able to follow all the steps in the [presentation video](http://bit.ly/2GCUBfK).

## Parsing the commands

You may not be able to see the commands in the video, so here is what I used.

On Darknet original install:

Detect Image:
```./darknet detector test cfg/voc.data cfg/tiny-yolo-voc.cfg backup/tiny-yolo-voc.weights data/dog.jpg
```
Webcam:
```./darknet detector demo cfg/voc.data cfg/tiny-yolo-voc.cfg backup/tiny-yolo-voc.weights
```

PyTorch-Yolo2:
```python demo.py cfg/tiny-yolo-voc.cfg tiny-yolo-voc.weights
```

Darkflow:
```./flow --model cfg/tiny-yolo-voc.cfg --load backup/tiny-yolo-voc.weights --demo camera
```

RectLabel - Pay the man, and then label your items. You'll need to add your object in settings first, load your folder, and then go crazy labeling. Remember the 'command-I' if you're doing a lot. It helps.

VOC_Label, convert pixel annotations to Yolo percentage annotations:
```python voc_label.py -p training/JackSkellington
```
Process training and test files (copy to same directory as images, without annotations folder in it):
```python process.py
```

Validate - AlexeyAb:
```./darknet detector map data/skellington.data cfg/skellington.cfg backup/skellington_1000.weights
```

```./darknet detector map data/skellington.data cfg/skellington.cfg backup/skellington_4000.weights
```

Jack Skellington Demo - PyTorch
You need to copy the demo.py file I included into your PyTorch Yolo2 folder. It has some quick changes to lower the threshold and pull the proper .data file.
```python demo.py cfg/skellington.cfg backup/skellington_4000.weights
```

I think that's about it. You should be able to figure out how to do your own custom objects from this. Feel free to post an issue if you run into any challenges.
