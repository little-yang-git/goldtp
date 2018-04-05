#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "Little.Yang"  

#====#====#====#====

import y_file
import y_find
# bb=y_file.in_csv("D:\Zihan\Desktop\\1.csv")
# y_file.out_csv("D:\Zihan\Desktop\\2.csv",bb)
dir="c:\\"
name=['.ini']
# print(y_find.find_main(dir))
print(y_find.find_files(dir,name))
# print(y_find.find_pdir(dir,name))
