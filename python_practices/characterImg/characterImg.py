#!/bin/python3
# -*- coding: UTF-8 -*-

from PIL import Image
import argparse

# 字符画中出现的字符
character_List = list("@a #^$>%/&*+-!\'")
#character_List = list("@ \'")

# 计算使用character_List的哪个字符
def getChar(r,g,b,alpha=256):
    if alpha == 0:
        return ' '

    # 得出字符组长度
    charList_Length = len(character_List)
    # 计算灰度值(此公式有很多)
    Gray = int(0.2126*r + 0.7152*g + 0.0722*b)
    # 计算灰度值与字符组长度的对应比
    U = (256.0 + 1) / charList_Length
    # 返回要使用的字符
    return character_List[int(Gray/U)]

# 创建一个解析对象
parser = argparse.ArgumentParser()
# 添加参数,每个add_argument()对应一个参数
# 输入文件/输出文件/输出宽度/输出高度
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width', type = int, default = 70)
parser.add_argument('--height', type = int, default = 60)
# 进行解析
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

if __name__ == '__main__':
    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT),Image.NEAREST)

    txt = ""

    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += getChar(*im.getpixel((j,i)))
        txt += '\n'

    print(txt)

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open('output.txt','w') as f:
            f.write(txt)
