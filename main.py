#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
# ====#====#====#====
# __author__ = "Little.Yang"  

# ====#====#====#====
import time

import y_file
import y_find

start = time.clock()

rootDir = "\\\\192.168.8.11\图片\整理"
f_name = "D:\桌面\\01.csv"
h_name = y_file.in_csv(f_name)
a_dir=y_find.find_pdir(rootDir,h_name)
print(type(a_dir))
y_file.out_csv('D:\\桌面\\02.csv',a_dir)

end = time.clock()
print("read: %f s" % (end - start))
