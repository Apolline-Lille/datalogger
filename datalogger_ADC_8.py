#!/usr/bin/python

version='v0.4.0'

import serial
import string
import time
import argparse

#path and device name
import xsensor_device
#path and file name
import xsensor_path

##set column names
#colnames(t)=c("time","index","NO2_1","NO2_2","PID",...)

#ADC 8 sensors

#CLI arguments
serialDev='/dev/ttyUSB0'
fake='test.raw'
module='ADC'+'_'+'A?00NNNN'
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
nb=8*2 #8 sensors
record=range(nb)
value=range(nb)

#get current time
current_time=time.localtime()
str_time=time.strftime('%Y/%m/%d %H:%M:%S\n',current_time)
print str_time

#set info file name from date
import platform
hostname=platform.node()
info_file_name=xsensor_path.get_info_file_name(current_time,hostname)

#set module name
module=(module.split('_'))[0] #from generic for Help
module=module+'_'+xsensor_device.get_serial_device_name(serialDev)

#write to information file
fi=open(info_file_name,"a")
fi.write(str_time);    fi.write(" ")
fi.write(serialDev);   fi.write(" ")
fi.write(module);      fi.write(" open\n")
fi.close() #information file

#set both raw and data file names from both module and date
file_name=xsensor_path.get_data_file_name(module,current_time)
raw_file_name=xsensor_path.get_raw_file_name(module,current_time)

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
  #get current time
  current_time=time.localtime()
  str_time=time.strftime('%Y/%m/%d %H:%M:%S',current_time)
  #check array validity
  if(len(value)!=(3+nb)):
    #print error
    print line
    print value
    print len(value)
    #write to information file
    fi=open(info_file_name,"a")
    fi.write(str_time);    fi.write(" ")
    fi.write(serialDev);   fi.write(" ")
    fi.write(module);
    fi.write(" error:|");
    fi.write(line);        fi.write("|\n")
    fi.close() #information file
    continue
  #generate module line from arrays
  line=module+";"+str_time+";"+str(iteration)
  line+=";"+value[1]
  line+=";"+value[2]
  for i in range(3,nb+3):
    line+=";"+value[i]
#    line+=";"+str(record[i])
  line+="\n"
  print line
  #setup file name from date
  file_name=xsensor_path.get_data_file_name(module,current_time)
  raw_file_name=xsensor_path.get_raw_file_name(module,current_time)
  #write to file
  fo=open(file_name,"a")
  fo.write(line)
  fo.close()
  #next record index
  iteration+=1
  time.sleep(0.5)

if(serialDev==fake): #test#
  ser.close()
