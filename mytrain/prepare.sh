#!/bin/bash

if [ $# != 1 ]; then
	echo "absolute images path needed"
	exit 0
fi

IMGPATH=$1
echo IMGPATH $IMGPATH

python3 creat_list.py $IMGPATH

python3 voc_label.py $IMGPATH


