#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import hashlib

# 方法一
str1 = "Hello Python"
md5 = hashlib.md5()
md5.update(str1.encode("utf-8"))
# md5.update(str1.encode("gbk"))
print(md5.hexdigest())

str1 = "Hello "
str2 = "Python"
md5 = hashlib.md5()
md5.update(str1.encode("utf-8"))
md5.update(str2.encode("utf-8"))
print(md5.hexdigest())

# sha256 同理
str1 = "Hello Python"
sha256 = hashlib.sha256()
sha256.update(str1.encode("utf-8"))
print(sha256.hexdigest())

# 方法二
str1 = "Hello Python"
print(hashlib.new("md5",str1.encode("utf-8")).hexdigest())

# 方法三
str1 = "Hello Python"
print( hashlib.md5(str1.encode("utf-8")).hexdigest() )

# 计算文件的md5 (小文件)
bfile = open('test.png', 'rb').read()
print( hashlib.md5(bfile).hexdigest() )


# 计算文件的md5 (大文件，如果文件较大，就不能一次性读入内存，必须分块)
BLOCKSIZE = 1025
md5 = hashlib.md5()
with open('test.png','rb') as stream:
    buffer = stream.read(BLOCKSIZE)
    while len(buffer) > 0 :
        md5.update(buffer)
        buffer = stream.read(BLOCKSIZE)
print(md5.hexdigest())


