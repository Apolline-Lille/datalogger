#!/usr/bin/python

import serial
import string
import time

#tail -n 24 2014_10_02.txt > test.txt

f=open('test.txt', 'r')
for line in f:
  print "line=", line

quit()

serialDev='/dev/ttyUSB0'
file_name="2014_10_01.txt"

ser = serial.Serial(serialDev, 115200, timeout=67)

print 'record all lines from ', serialDev

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

print 'start reading serial ...'

while(True):
  #wait and get data
  line=ser.readline()
  #show
  print line
  #get information
  values=strsplit(line,'|')
  if(i==12):
    #setup file name from date
    file_name=time.strftime('%Y_%m_%d.txt',time.localtime())
  #write to file
  f=open(file_name,"a")
  f.write(line)
  f.close()
