#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************



n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

n = n//2
tem = n-1
res = 0
for i in range(n):
    res += tem
    tem -= 1
print(res)
