#!/usr/bin/python

version='v0.3.9'

import serial
import string
import time
import argparse

#path and device name
import xsensor_device
#path and file name
import xsensor_path

#CLI, static and time names
def command_line(serialDev,fake, module):
  hostname='raspc2aN'
  current_time=time.localtime()
  info_file_name=xsensor_path.get_info_file_name(current_time,hostname)
  file_name=xsensor_path.get_data_file_name(module,current_time)
  raw_file_name=xsensor_path.get_raw_file_name(module,current_time)
  parser = argparse.ArgumentParser(
    description='log data from ArduinoDUE/PAR sensor.'
    +' At least, 3 files will be written:'
    +' 1. single information file (.info),'
    +' 2. one raw sensor ouput (.raw) file per day,'
    +' 3. one data (.txt) file per day.'
   ,epilog='example: %(prog)s --device '+serialDev
    +'  #will write e.g. module #'+module+' data as 1."'
    +info_file_name+'", 2."'+file_name+'" and 3."'+raw_file_name+'" files.'
    )
  parser.add_argument('-d','--device',default=serialDev, help='USB device name or '+fake+' (e.g. '+serialDev+')')
  parser.add_argument('-v','--version',action='version',version='%(prog)s '+version)
  return hostname, current_time, info_file_name,file_name,raw_file_name,parser.parse_args()


#script call
if __name__ == "__main__":
  #dev init
  serialDev='/dev/ttyUSB0'
  fake='test.raw'
  module='DYLOS'+'_'+'dylosN'
  hostname, current_time, info_file_name,file_name,raw_file_name, args=command_line(serialDev,fake,module)
  print current_time

