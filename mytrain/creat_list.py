# coding:utf-8

import os
from os import listdir, getcwd
from os.path import join
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ', sys.argv[0], '/data/VOCdevkit/VOC2007/')
        sys.exit(0)

    IMGPATH = sys.argv[1]

    source_folder = IMGPATH + '/Annotations'
    train_txt = IMGPATH + '/ImageSets/Main/train.txt'
    val_txt = IMGPATH + '/ImageSets/Main/val.txt'
    test_txt = IMGPATH + '/ImageSets/Main/test.txt'
    file_list = os.listdir(source_folder)
    xml_cnt = len(file_list)
    train_cnt = 0
    val_cnt = 0
    test_cnt = 0
    xml_no = []

    for file_obj in file_list:
        file_path = os.path.join(source_folder, file_obj)
        file_name, file_extend = os.path.splitext(file_obj)
        xml_no.append(file_name)

    train_no = xml_no[0:int(xml_cnt / 2)]
    val_no = xml_no[int(xml_cnt / 2):(int(xml_cnt / 2) + int(xml_cnt / 4))]
    test_no = xml_no[(int(xml_cnt / 2) + int(xml_cnt / 4)):]

    with open(train_txt, 'w') as train_file:
        with open(val_txt, 'w') as val_file:
            with open(test_txt, 'w') as test_file:

                for n in train_no:
                    train_cnt = train_cnt + 1
                    train_file.write(n + '\n')
                for n in val_no:
                    val_cnt = val_cnt + 1
                    val_file.write(n + '\n')
                for n in test_no:
                    test_cnt = test_cnt + 1
                    test_file.write(n + '\n')

print('train_cnt', train_cnt)
print('val_cnt', val_cnt)
print('test_cnt', test_cnt)
