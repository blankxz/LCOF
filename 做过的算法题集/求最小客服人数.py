#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def calcMinStaff():
    n = int(input())
    data = []
    for i in range(n):
        data.append(list(map(int,input().split(','))))
    data.sort(key = lambda k:k[1])
    res = 0
    m = data[0][1]
    for i in range(n-1):
        if m < data[i][0]:
            m = data[i][0]
        if data[i+1][0] > m:
            continue
        else:
            res += 1
    return res

# ******************************结束写代码******************************


res = calcMinStaff()

print(str(res) + "\n")