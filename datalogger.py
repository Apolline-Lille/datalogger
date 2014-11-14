#!/usr/bin/python

version='v0.3.0'

import serial
import string
import time
import argparse

##set column names
#colnames(t)=c("time","index","PID")

#Alphasense PID

#path and file name
def get_file_name_base(module_name,current_time):
  return time.strftime('%Y/%m/',current_time)+module_name+time.strftime('%Y_%m_%d',current_time)

def get_data_file_name(module_name,current_time):
  return get_file_name_base(module_name+'_',current_time)+'.txt'

def get_raw_file_name(module_name,current_time):
  return get_file_name_base(module_name+'_',current_time)+'.raw'

def get_info_file_name(current_time):
  return get_file_name_base('',current_time)+'.info'

#CLI arguments
serialDev='/dev/ttyUSB0'
fake='test.raw'
module='PID'
current_time=time.localtime()
info_file_name=get_info_file_name(current_time)
file_name=get_data_file_name(module,current_time)
raw_file_name=get_raw_file_name(module,current_time)
parser = argparse.ArgumentParser(
  description='log data from NDIR/CO2 sensor.'
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
args = parser.parse_args()

##--device CLI argument
serialDev=args.device
if(serialDev==fake): #test#
  print 'test' #test#
  ser=open(fake, 'r') #test#
else:
  ser=serial.Serial(serialDev, 9600, timeout=12)
print 'pack module lines from ', serialDev

#sensor parameter arrays
nb=2 #1 sensors and others
record=range(nb)
value=range(nb)

#get current time
current_time=time.localtime()
str_time=time.strftime('%Y/%m/%d %H:%M:%S\n',current_time)
print str_time

#set info file name from date
info_file_name=get_info_file_name(current_time)

#write to information file
fi=open(info_file_name,"a")
fi.write(str_time)
fi.write(serialDev)
fi.write(module)
fi.close() #information file

#set both raw and data file names from both module and date
file_name=get_data_file_name(module,current_time)
raw_file_name=get_raw_file_name(module,current_time)

iteration=0

if(serialDev==fake): #test#
  mode=fake
else:
  mode='serial'
print 'start reading '+mode+' ...'
while(True): #loop on both sensors and time
  #wait and get data
  line=ser.readline()
  #exit at end of file
  if not line: break
  #show
  #print "|",line,"|"
  #write to raw file
  fr=open(raw_file_name,"a")
  fr.write(line)
  fr.close()
  #add sensor parameters in arrays
  line=line.replace("\r\n","")
  value=line.split(";")
#  print value
#  record[i]=float(value[i])
  #generate module line from arrays
  current_time=time.localtime()
  str_time=time.strftime('%Y/%m/%d %H:%M:%S',current_time)
  line=module+";"+str_time+";"+str(iteration)
  line+=";"+value[2]
#  for i in range(0,nb-1):
#    line+=";"+value[i]
#    line+=";"+str(record[i])
  line+="\n"
  print line
  #setup file name from date
  file_name=get_data_file_name(module,current_time)
  raw_file_name=get_raw_file_name(module,current_time)
  #write to file
  fo=open(file_name,"a")
  fo.write(line)
  fo.close()
  #next record index
  iteration+=1
  time.sleep(0.5)

if(serialDev==fake): #test#
  ser.close()
