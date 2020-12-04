import os
import re
import sys

fileList = os.listdir(r"./video")
# 输出此文件夹中包含的文件名称
print("修改前：" ,fileList)
# 得到当前工作目录
currentpath = os.getcwd()
# 将当前工作目录修改为待修改文件夹的位置
os.chdir(r"./video")
#定义正则表达式 --> Cloudbabies.S01E01.Fly.Away.Home[www.lxwc.com.cn].avi
renameRegex = re.compile(r'(.*)(\[www.lxwc.com.cn\])(\.avi)')
# 遍历文件夹中所有文件
for fileName in fileList:
    mo = re.search(renameRegex, fileName)
    newName = mo.group(1)+mo.group(3)
    print(newName)
    # 文件重新命名
    os.rename(fileName,newName)
print("***************************************")
# 改回程序运行前的工作目录
os.chdir(currentpath)
# 刷新
sys.stdin.flush()
# 输出修改后文件夹中包含的文件名称
print("修改后：" + str(os.listdir(r"./video")))
