#!/usr/bin/python

version='v0.0.0'

import string
import subprocess
import argparse

##path and file name
#def get_file_name_base(module_name,current_time):
#  return time.strftime('%Y/%m/',current_time)+module_name+time.strftime('%Y_%m_%d',current_time)


list=subprocess.check_output(["ls","-lah","/dev/serial/by-id"])
#print list

list=list.splitlines()
#print list

device_name=[]
device_path=[]
for i in range(3,len(list)):
  #print list[i]
  tmp=list[i].split(" ")
  device_name.append(tmp[9])
  device_path.append(tmp[11])

for i in range(0,len(device_name)):
  print device_name[i], device_path[i]

