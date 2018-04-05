#! /usr/bin/env python  
# -*- coding:utf-8 -*-  
#====#====#====#====  
# __author__ = "Little.Yang"  

#====#====#====#====
import time
import os

def find_pdir(rootDir,name,c=0,lx=0):
	f_path,f_file=find_main(rootDir)
	dir_hall,dir_kall=p_dir(f_path)
	a_dir={}
	for i in name:
		if lx==0:
			if i[c] in dir_hall.keys():
				a_dir[i[c]]=dir_hall[i[c]]
			else:
				a_dir[i[c]]='NoFiles'
		else:
			if i[c] in dir_kall.keys():
				a_dir[i[c]]=dir_kall[i[c]]
			else:
				a_dir[i[c]]='NoFiles'
	return a_dir

def p_dir(path={}):
	dir_hall={}
	dir_kall={}
	for k,v in path.items():
		dir_h=str(k)
		if dir_h.find("#")>=0:
			dir_h=dir_h[:dir_h.find("#")]
			dir_kh=dir_h[:dir_h.rfind("#")]
		else:
			dir_kh=dir_h
		if os.path.exists(str(v)+'\\1#.jpg'):
			dir_n="|1"
		elif os.path.exists(str(v)+'\\2#.jpg'):
			dir_n="|2"
		else:
			dir_n="|0"
		dir_hall[dir_h]=str(v)+dir_n
		dir_kall[dir_kh]=str(v)+dir_n
	return dir_hall,dir_kall

def find_main(rootDir):
	f_file={}
	f_path={}
	for root,dirs,files in os.walk(rootDir):
		for file in files:
			f_file[file]=os.path.join(root,file)
		for dir in dirs:
			f_path[dir]=os.path.join(root,dir)
			find_main(dir)
	return f_path,f_file

def find_files(rootdir,name=list):
	refile={}
	f_path,f_file=find_main(rootdir)
	for i in name:
		if i in f_file.keys():
			refile[i]=f_file[i]
		else:
			refile[i]='NoFile'
	return refile

