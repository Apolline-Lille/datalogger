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

#sensor parameter arrays
nb=13 #12 sensors and others
record=range(nb)
value=range(nb)

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

##while(True): #loop on both sensors and time
##  #wait and get data
##  line=ser.readline()

f=open('test.txt', 'r') #test#
for line in f:

  #show
  print line
  #skip empty lines
  if(len(line)<12):
    continue
  #get information
  values=line.split('|')
  module=values[0]
  index=int(values[2]) #sensor, see colnames
  if(index==1): #new record start
    #get record time
    current_time=time.localtime()
    #clear module array
    for i in xrange(0,len(record)):
      record[i]=0
    for i in xrange(0,len(value)):
      value[i]=''
  #add sensor parameters in arrays
  record[index]=int(values[1])
  value[index]=values[3].replace("\n","")
  #write to file
  if(index==12): #new record stop
    print 'generate module line from array'
    str_time=time.strftime('%Y/%m/%d %H:%M:%S',current_time)
    line=module+" @ "+str_time+"\t"+str(record[index])
    print line
    #setup file name from date
    file_name=time.strftime('%Y_%m_%d.txt',current_time)
    #write to file
    f=open(file_name,"a")
    f.write(line)
    f.close()

print "index=",index
print "record=",record
print "value=",value
