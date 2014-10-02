#!/usr/bin/python

import serial
import string
import time

#tail -n 24 2014_10_02.txt > test.txt

##set column names
#colnames(t)=c("time","index","battery","temperature","humidity",
#  "TGS4161","TGS2620","MICS2610","TGS2602","MICS2710","TGS2442",
#  "record")

##serialDev='/dev/ttyUSB0'
##ser = serial.Serial(serialDev, 115200, timeout=67)
##print 'pack module lines from ', serialDev

#get current time
current_time=time.localtime()
str_time=time.strftime('%Y/%m/%d %H:%M:%S\n',current_time)
print str_time
#setup file name from date
file_name=time.strftime('%Y_%m_%d.txt',current_time)
#write to file
f=open(file_name,"a")
f.write(str_time)
f.close()

##print 'start reading serial ...'

##while(True):
##  #wait and get data
##  line=ser.readline()

f=open('test.txt', 'r') #test
for line in f:

  #show
  print line
  #skip empty lines
  if(len(line)<12):
    continue
  #get information
  values=line.split('|')
  module=values[0]
  record=values[1]
  index=int(values[2]) #sensor, see colnames
  value=values[3]
  if(index==1):
    #prm[index]=
    print 'get record date'
    print 'clear module array'
  print 'add sensor prms in array'
  #setup file name
  if(index==12):
    print 'generate module line from array'
    line=record
    print line
    #write to file
    f=open(file_name,"a")
    f.write(line)
    f.close()
    #setup file name from date
    file_name=time.strftime('%Y_%m_%d.txt',time.localtime())
