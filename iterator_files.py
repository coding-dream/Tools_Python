#-*- coding: UTF-8 -*-
import os

path = "D:\BTSyntcFolder\IT"
# 三个参数：1.父目录 2.当前path下的所有文件夹名字（仅名字,不包含文件） 3.所有文件名字(不含路径)

for root,dirs,files in os.walk(path):
	for name in files:
		print(os.path.join(root, name).replace("D:\BTSyntcFolder\IT\\",""))

