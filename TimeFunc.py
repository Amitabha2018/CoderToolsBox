#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2023-02-25 14:56'

def sechms(seconds):
    '''
    Converting seconds into hour-minute-second format
    :param seconds: time in seconds
    :return: string  5h/3min/23s
    '''
    m,s = divmod(int(seconds),60)
    h,m = divmod(m,60)
    hms = "{}h/{}min/{}s".format(h,m,s)
    return hms
if __name__ == '__main__':
    hms = sechms(775.049516815)
    print(hms)
