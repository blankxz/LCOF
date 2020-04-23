import os
import time

def getFileSize(filePath):
    return os.path.getsize(filePath)/(1024**2)

def getFileCreateTime(filePath):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getctime(filePath)))

def getFileAccessTime(filePath):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getatime(filePath)))

def getFileModifyTime(filePath):
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(os.path.getmtime(filePath)))


print(getFileSize('程序设计.py'))
print(getFileCreateTime('程序设计.py'))
print(getFileAccessTime('程序设计.py'))
print(getFileModifyTime('程序设计.py'))