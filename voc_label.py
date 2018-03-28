import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from natsort import natsorted, ns
import argparse

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--path", type=str, default="images/", required=True,
    help="folder path for images")
args = vars(ap.parse_args())

# Change the classes here to whatever is in the RectLabel list
classes = ["Jack Skellington"]

current_directory =  os.path.dirname(os.path.realpath(__file__))
images = os.listdir(os.path.join(current_directory, args["path"]))
images = natsorted(images, key=lambda y: y.lower())

# This is only for Macs and the .DS_Store file that gets added to array
if '.DS_Store' in images:
    images.remove('.DS_Store')

# Remove _annotations, _labels folders and any text files for RectLabel
if '_annotations' in images:
    images.remove('_annotations')

# Remove _annotations, _labels folders and any text files for RectLabel
if 'annotations' in images:
    images.remove('annotations')

if '_labels' in images:
    images.remove('_labels')
    # images.remove('*.txt')

if 'labels' in images:
    images.remove('labels')
    # images.remove('*.txt')

for i, image in enumerate(images):
    images[i] = image[:-4]

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

def convert_annotation(image):
    in_file = open(os.path.join(args["path"], 'annotations/%s.xml'%(image)))
    out_file = open(os.path.join(args["path"], 'labels/%s.txt'%(image)), 'w')
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')

wd = getcwd()

for image in images:
    if not os.path.exists(os.path.join(args["path"], 'labels')):
        os.makedirs(os.path.join(args["path"], 'labels'))

    convert_annotation(image)
