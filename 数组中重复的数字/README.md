# 数组中重复的数字

## 题目描述

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

## 题解

### 方法一

先排序，然后看相邻元素是否有相同的，有直接return。时间O(nlogn)，空间O(1)

### 方法二

字典哈希表，时间O(1)，空间O(n)

### 方法三

0~n-1数字，把这些数字分别放在相应下标上，如nums[0]=0,nums[1]=1，如果num[0]!=0，则循环置换，令nums[nums[0]], nums[0] = nums[0], nums[nums[0]]，如发现相同数，则直接return