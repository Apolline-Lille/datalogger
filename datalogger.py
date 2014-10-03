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

#setup file names from date
file_name=time.strftime('%Y_%m_%d.txt',current_time)
raw_file_name=time.strftime('%Y_%m_%d.raw',current_time)
info_file_name=time.strftime('%Y_%m_%d.info',current_time)

#write to information file
fi=open(info_file_name,"a")
fi.write(str_time)

#get module start-up lines

f=open('test.txt', 'r') #test#
for line in f:
  #write to raw file
  fr=open(raw_file_name,"a")
  fr.write(line)
  fr.close()
  #write to information file
  fi.write(line)
  if(line.find('|')>0): #parameter line if containing character '|'
    break
fi.close() #information file

iteration=0

##print 'start reading serial ...'
##while(True): #loop on both sensors and time
##  #wait and get data
##  line=ser.readline()

for line in f:

  #show
  ##print line
  #write to raw file
  fr=open(raw_file_name,"a")
  fr.write(line)
  fr.close()
  #skip empty lines
  if(len(line)<6):
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
    #generate module line from array
    str_time=time.strftime('%Y/%m/%d %H:%M:%S',current_time)
    line=module+" @ "+str_time+"\t"+str(iteration)
    for i in xrange(5,len(value)):
      line+="\t"+value[i]
    line+="\t"+str(record[index])
    line+="\n"
    print line
    #setup file name from date
    file_name=time.strftime('%Y_%m_%d.txt',current_time)
    raw_file_name=time.strftime('%Y_%m_%d.raw',current_time)
    #write to file
    fo=open(file_name,"a")
    fo.write(line)
    fo.close()
    #next record index
    iteration+=1

f.close() #previous recorded file #test#

quit()

print "index=",index
print "record=",record
print "value=",value
