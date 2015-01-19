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

#--device CLI argument
def open_dev(args, serialDev,fake):
  serialDev=args.device
  if(serialDev==fake): #test#
    print 'test' #test#
    ser=open(fake, 'r') #test#
  else:
    ser=serial.Serial(serialDev, 9600, timeout=64)
  print 'pack module lines from ', serialDev
  return ser

#sensor parameter arrays
def arrays(size):
  nb=size #number of sensors
  record=range(nb)
  value=range(nb)
  return nb,record,value

def log_info(module):
  #get current time
  current_time=time.localtime()
  str_time=time.strftime('%Y/%m/%d %H:%M:%S\n',current_time)
  print str_time

  #set info file name from date
  import platform
  hostname=platform.node()
  info_file_name=xsensor_path.get_info_file_name(current_time,hostname)

  print info_file_name

  #write to information file
  fi=open(info_file_name,"a")
  fi.write(str_time);    fi.write(" ")
  fi.write(serialDev);   fi.write(" ")
  fi.write(module);      fi.write(" open\n")
  fi.close() #information file

#script call
if __name__ == "__main__":
  #dev init
  serialDev='/dev/ttyUSB0'
  fake='test.raw'
  module='DYLOS'+'_'+'dylosN' #generic module name
  hostname, current_time, info_file_name,file_name,raw_file_name, args=command_line(serialDev,fake,module) #Help and others

  #open pipe
  ser=open_dev(args, serialDev,fake)
  #sensor parameter arrays
  nb,record,value=arrays(2)

  #set module name
  module=(module.split('_'))[0] #from generic for Help
  module=module+'_'+xsensor_device.get_serial_device_name(serialDev)

  log_info(module)

  #set both raw and data file names from both module and date
  file_name=xsensor_path.get_data_file_name(module,current_time)
  raw_file_name=xsensor_path.get_raw_file_name(module,current_time)

  iteration=0
