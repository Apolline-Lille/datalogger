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
  device_name[i]=device_name[i].strip('usb-ifport0')
  device_path[i]='/dev/'+device_path[i].strip('../../')
  #Dylos
  template='Prolific_Technology_Inc._USB-Serial_Controller_D'
  if(device_name[i].rfind(template)==0):
    device_name[i]='DYLOS'
  #FTDI_FT232R: WaspMote, AlphaSenseCO2, MX3cK/ADC
  template='FTDI_FT232R_USB_UART_'
  if(device_name[i].rfind(template)==0):
    device_name[i]=device_name[i].replace(template,'')
  print device_name[i], device_path[i]

