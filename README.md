![Darknet Logo](http://pjreddie.com/media/files/darknet-black-small.png)

#Darknet#
Darknet is an open source neural network framework written in C and CUDA. It is fast, easy to install, and supports CPU and GPU computation.

For more information see the [Darknet project website](http://pjreddie.com/darknet).

For questions or issues please use the [Google Group](https://groups.google.com/forum/#!forum/darknet).

# 使用GPU时设置环境变量

export PATH=/usr/local/cuda-8.0/bin:$PATH

export LD_LIBRARY_PATH=/usr/local/cuda-8.0/lib64:$LD_LIBRARY_PATH

# 1个分类的训练脚本

mytrain/prepare.sh

mytrain/creat_list.py

mytrain/voc_label.py

mytrain/train.sh


