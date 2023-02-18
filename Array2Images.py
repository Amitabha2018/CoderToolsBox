#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2023-02-18 12:32'
import os
import tensorflow.compat.v1 as tf
import matplotlib.pyplot as plt
from PIL import Imagefrom
from tqdm import tqdm

def array2image(images,labels,class_nums,save_dir):
    '''
    images: images in the form of arrays
    labels: labels in the form of arrays
    class_num: number of categories
    save_dir: storage path for datasets in image form
    '''
    #setting savedir
    for i in range(class_nums):
        dir_path = os.path.join(save_dir,str(i))
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
    #saving images
    class_count = [0]*class_nums
    for i in tqdm(range(len(images))):
        img_array = images[i]*255
        class_count[labels[i]] += 1
        img = Image.fromarray(img_array,'L')
        dir_path =os.path.join(save_dir,str(labels[i]))
        img_name = str(labels[i])+'_'+str(class_count[labels[i]])+'.jpg'
        save_path = os.path.join(dir_path,img_name)
        img.save(save_path)


if __name__ == "__main__":
    (train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()
    train_dir = '/home/user/lab/noisylabel/datasets/MNIST_IMAGES/train'
    test_dir = '/home/user/lab/noisylabel/datasets/MNIST_IMAGES/test'
    class_nums = len(set(train_labels))
    array2image(train_images, train_labels, class_nums, train_dir)
    array2image(test_images, test_labels, class_nums, test_dir)