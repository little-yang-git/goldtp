#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "Little.Yang"  

#====#====#====#====

import csv
from itertools import islice

def in_csv(filename):
	csv_file=csv.reader(open(filename,'r'))
	csv_txt=[x for x in islice(csv_file,1,None)]
	return csv_txt

def out_csv(filename,list):
	out=open(filename,"a",newline="")
	writer=csv.writer(out,dialect="excel")
	writer.writerow(['货号','路径'])
	writer.writerows(list)
	# for k,v in dist.items():
	# 	writer.writerow([k,v])

