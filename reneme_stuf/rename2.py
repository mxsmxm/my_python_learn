import os

import re

import sys

import argparse

# 获取命令行参数
parser = argparse.ArgumentParser() 
parser.add_argument('--filder',help = '传入目录参数') 
parser.add_argument('--num',help='传入需要添加在文件名前的数字')
args = parser.parse_args() 

fileList = os.listdir('./'+args.filder)

# 输出此文件夹中包含的文件名称

print("修改前：" ,fileList)

# 得到当前工作目录

currentpath = os.getcwd()

# 将当前工作目录修改为待修改文件夹的位置

os.chdir('./'+args.filder)


# 遍历文件夹中所有文件

for fileName in fileList:


    newName = args.num + fileName

    print(newName)

    # 文件重新命名

    os.rename(fileName,newName)

print("***************************************")

# 改回程序运行前的工作目录

os.chdir(currentpath)

# 刷新

sys.stdin.flush()

# 输出修改后文件夹中包含的文件名称

print("修改后：" + str(os.listdir('./'+args.filder)))