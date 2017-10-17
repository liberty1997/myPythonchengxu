#!/bin/python3

import os 

path = r'/home/liberty/.wallpaper/'

# 图片格式
image_format = ['png', 'jpg', 'jpeg']

# 找到path路径下所有符合的图片并把文件名排序
files = [i for i in os.listdir(path) if i.split('.')[-1] in image_format]
files.sort()

for i in range(len(files)):
	# 得到本张图片的格式
	i_f = image_format.index(files[i].split('.')[-1])

	# 新文件名
	new = r'wallpaper_' + str(i+1).zfill(3) + '.' + image_format[i_f]
	
	# 重命名
	os.rename(path+files[i], path+new)
