#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2024-01-12 10:14'


def path2windows(path):
    '''
    path: the path of Linux in the form of string
    '''
    wpath = path.replace('/', '\\')
    return wpath





if __name__ == "__main__":
    print("hello world")
    p = 'G:\\Clothing-1M\\images/2/11/815467435,1984292211.jpg'
    print(path2windows(p))