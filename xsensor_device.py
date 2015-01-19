#!/usr/bin/python

version='v0.0.2'

import string
import subprocess

#path and device name
def get_serial_pathNdevice_names():
  #list serial devices by id (e.g. POSIX OS)
  list=subprocess.check_output(["ls","-lah","/dev/serial/by-id"])
#  print list

  #make list as a list
  list=list.splitlines()
#  print list

  #get device and name
  device_name=[]
  device_path=[]
  for i in range(3,len(list)):
  #  print list[i]
    tmp=list[i].split(" ")
    device_name.append(tmp[8])
  #  print device_name[i-3]
    device_path.append(tmp[10])
  #  print device_path[i-3]

  #pack device name
  for i in range(0,len(device_name)):
    #clean name
    device_name[i]=device_name[i].strip('usb-ifport0')
    device_path[i]='/dev/'+device_path[i].strip('../../')
    #specific name cleaning
    ##Dylos
    template='Prolific_Technology_Inc._USB-Serial_Controller_D'
    if(device_name[i].rfind(template)==0):
      device_name[i]='dylos0'
    ##FTDI_FT232R: WaspMote, AlphaSenseCO2, MX3cK/ADC
    template='FTDI_FT232R_USB_UART_'
    if(device_name[i].rfind(template)==0):
      device_name[i]=device_name[i].replace(template,'')
  #  print device_name[i], device_path[i]

  return device_path,device_name

def get_serial_device_name(path):
  device_path,device_name=get_serial_pathNdevice_names()
#BUG TODO:
  #while(path==device_path)
  return device_name[0]

#script call
if __name__ == "__main__":
  device_path,device_name=get_serial_pathNdevice_names()
  for i in range(0,len(device_name)):
    print device_name[i], device_path[i]
