#DropboxからBOXへディレクトリ同期

import glob
import os
import subprocess

original_home = "/Users/kato/Box/Kato_mih/"
#Ext_dir = "/Users/eiryokawakami/Box/Ext_101212_Health Data Mathematical Reasoning Team/"
#Int_dir = "/Users/eiryokawakami/Box/Int_101212_Health Data Mathematical Reasoning Team/"
Per_dir = "/Users/kato/Box/Kato/"

#Ext_dir_list_file = "Ext_dir.txt"
#Int_dir_list_file = "Int_dir.txt"
Per_dir_list_file = "Per_dir.txt"

#Ext_dir_list = []

#with open(Ext_dir_list_file,'r') as fi:
#	line = fi.readline()
#	while line:
#		Ext_dir_list.append(line[:-1])
#		line = fi.readline()

#Int_dir_list = []

#	line = fi.readline()
#	while line:
#		Int_dir_list.append(line[:-1])
#		line = fi.readline()

Per_dir_list = []
with open(Per_dir_list_file,'r') as fi:
    line = fi.readline()
    while line:
        Per_dir_list.append(line[:-1])
        line = fi.readline()

os.chdir(original_home)

original_files = glob.glob("*")

#print(Ext_dir_list)

#for f in original_files:
#	if f in Ext_dir_list:
#		print(f)
#		cmd =['rsync','-auvrH','--progress',f,Ext_dir]
#		proc = subprocess.run(cmd)
#	elif f in Int_dir_list:
#		print(f)
#		cmd =['rsync','-auvrH','--progress',f,Int_dir]
#		proc = subprocess.run(cmd)
#	else:
#		print(f)
#		cmd =['rsync','-auvrH','--progress',f,Per_dir]
#		proc = subprocess.run(cmd)

for f in original_files:	
    if f in Per_dir_list:
        print(f)
        cmd =['rsync','-auvrH','--progress',f,Per_dir]
        proc = subprocess.run(cmd)
    else:
        print('> Not my own file :' + f)