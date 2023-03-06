#!/usr/bin/env python
# -*- coding:utf-8 -*-  
__author__ = 'IT小叮当'
__time__ = '2023-03-06 20:06'

# python 计算两个相同长度列表有多少个元素不同   计算不同元素个数占列表长度的百分比
# 可以使用zip函数来计算两个相同长度列表中有多少个元素不同。
# 具体来说，我们可以将这两个列表压缩成一个元组列表，然后在循环中检查每个元组中的元素是否相等。
# 如果不相等，则计数器加1。最后，我们可以将计数器除以列表长度，得到不同元素个数占列表长度的百分比。

def look_differ_list(list1,list2):
    '''
    list1: List type
    list2: List type
    return diff_count,percent_diff
    diff_count: The number of elements that differ between two lists
    percent_diff: Percentage of the length of the list with distinct elements
    Note that: list1 and list2 are required to have the same length
    '''

    diff_count = 0
    for x, y in zip(list1, list2):
        if x != y:
            diff_count += 1

    percent_diff = diff_count / len(list1) * 100

    return diff_count,percent_diff


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 4, 4, 6]
    diff_count,percent_diff = look_differ_list(list1,list2)

    print('不同元素的数量:', diff_count)
    print('不同元素的百分比:', percent_diff)

