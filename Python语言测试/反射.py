#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: rex.cheny
# E-mail: rex.cheny@outlook.com

class TestObj(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def displayName(self):
        print("displayName方法执行，打印姓名：", self.name)



def AAA(self):
    print("I am AAA.")


def main():
    to = TestObj("Tom", 23)
    # 查看 to 实例里面是否有 name 这个属性
    if hasattr(to, "name"):
        print("实例 to 中有 name 属性。")
        print(getattr(to, "name"))
    else:
        print("实例 to 中没有 name 属性。")

    if hasattr(to, "displayName"):
        print("实例 to 中有 displayName 属性。")
        getattr(to, "displayName")()
    else:
        print("实例 to 中没有 displayName 属性。")

    if hasattr(to, "AAA"):
        print("实例 to 中有 AAA 属性。")
        getattr(to, "AAA")()
    else:
        print("实例 to 中没有 AAA 属性，将会设置。")
        setattr(to, "AAA", AAA)  # 参数：实例、方法名称、具体方法  相当于 to.AAA = AAA 第一个AAA是函数在实例中的名称， 第二个AAA是把哪个函数放进去，两者只是恰好这里名称一样

        # to.AAA(to)  # 这里一定要主动传递一个实例进去，因为它不会自动装配self
        getattr(to, "AAA")(to)


if __name__ == '__main__':
    main()