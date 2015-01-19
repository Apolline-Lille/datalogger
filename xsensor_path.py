#!/usr/bin/python

version='v0.1.0'

import string
import os
import time
import argparse

#path and file name
def get_path_name_base(current_time):
  path=time.strftime('%Y/%m/',current_time)
  #path exist
  if(not os.access(path,os.F_OK)):
    os.makedirs(path)
  return path

def get_file_name_base(module_name,current_time):
  return get_path_name_base(current_time)+module_name+time.strftime('%Y_%m_%d',current_time)

def get_data_file_name(module_name,current_time):
  return get_file_name_base(module_name+'_',current_time)+'.txt'

def get_raw_file_name(module_name,current_time):
  return get_file_name_base(module_name+'_',current_time)+'.raw'

def get_info_file_name(current_time,hostname):
  return get_file_name_base(hostname+'_',current_time)+'.info'
