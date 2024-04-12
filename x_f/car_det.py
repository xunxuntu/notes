# -*- coding: utf-8 -*-
"""
    @File : car_det.py
    @Time : 2024-04-12
    Description : 
"""

# 从coco128中提取车类的image和label
# 0 bicycle
# 1 car
# 2 motorcycle
# 3 bus
# 4 truck

import os
from shutil import copyfile

src_path = './coco128/labels/train2017/'  # 标签
img_path = './coco128/images/train2017/'  # 图像
dst_label_path = './traffic_train_coco128/labels/'
dst_img_path = './traffic_train_coco128/images/'
cls_id = ['1', '2', '3', '5', '7']  # bicycle car motorcycle bus truck

labels = os.listdir(src_path)
labels.sort()

for label in labels:
    if label[-1] != 't':
        continue
    # 存标签
    tmp = []
    for line in open(src_path + '/' + label):
        str_list = line.split()
        # 被选类别的标签
        for i in range(len(cls_id)):
            if str_list[0] == cls_id[i]:
                # 改成自己的标签，这里是数组下标
                line = str(i) + line[1:]
                tmp.append(line)
    # 没有被选类别
    if len(tmp) < 1:
        continue
    # 新的标签文件
    with open(dst_label_path + label, 'w') as f:
        for item in tmp:
            f.write(item)
    #f.close()
    image = label[:-4] + '.jpg'
    # 拷贝有被选类别的图片
    copyfile(img_path + '/' + image, dst_img_path + image)

