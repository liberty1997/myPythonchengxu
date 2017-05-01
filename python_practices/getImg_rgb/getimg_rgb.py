#!/bin/python3
# -*- coding: UTF-8 -*-
from PIL import Image
width = 60
height = 60
im = Image.open(input("Input an image's path:('\\' escape as '\\\\')\n"))
im = im.resize((width,height),Image.NEAREST)
for i in range(height):
    for j in range(width):
        print(im.getpixel((i,j)), end=' ')
    print('\n')
