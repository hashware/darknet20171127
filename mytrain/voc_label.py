# coding:utf-8

import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import sys

if len(sys.argv) != 2:
    print('usage: ', sys.argv[0], '/data/VOCdevkit/VOC2007/')
    sys.exit(0)

IMGPATH = sys.argv[1]
if IMGPATH[0] != '/':
    print('use absolute path')
    sys.exit(0)

sets = ['train', 'val', 'test']

classes = []
with open('label.names', 'r') as f:
    lines = f.readlines()
    for line in lines:
        classes.append(line.strip())

print('classes', classes)


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(imgpath, image_id):
    in_file = open('%s/Annotations/%s.xml' % (imgpath, image_id))
    out_file = open('%s/labels/%s.txt' % (imgpath, image_id), 'w')
    tree = ET.parse(in_file)
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
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


wd = getcwd()

for image_set in sets:
    if not os.path.exists('%s/labels/' % (IMGPATH,)):
        os.makedirs('%s/labels/' % (IMGPATH,))
    image_ids = open('%s/ImageSets/Main/%s.txt' % (IMGPATH, image_set)).read().strip().split()
    list_file = open('to_%s.txt' % (image_set,), 'w')
    for image_id in image_ids:
        list_file.write('%s/JPEGImages/%s.jpg\n' % (IMGPATH, image_id))
        convert_annotation(IMGPATH, image_id)
    list_file.close()

os.system("cat to_train.txt to_val.txt > train.txt")
os.system("cat to_train.txt to_val.txt to_test.txt > train.all.txt")
