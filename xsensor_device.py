#!/usr/bin/python

version='v0.0.3'

import string
import subprocess

#path and device name
def get_serial_pathNdevice_names():
  #list serial devices by id (e.g. POSIX OS)
  list=subprocess.check_output(["ls","-l","--time-style=iso","/dev/serial/by-id"])
#  print list

  #make list as a list
  list=list.splitlines()
#  print list

  #get device and name
  device_name=[]
  device_path=[]
  for i in range(1,len(list)):
  #  print list[i]
    tmp=list[i].split(" ")
    device_name.append(tmp[7])
  #  print device_name[i-1]
    device_path.append(tmp[9])
  #  print device_path[i-1]

  #pack device name
  for i in range(0,len(device_name)):
    #clean name
    device_name[i]=device_name[i].replace('usb-','')
    device_name[i]=device_name[i].replace('if','')
    device_name[i]=device_name[i].replace('port','')
    device_name[i]=device_name[i].rstrip('0')
    device_name[i]=device_name[i].replace('-','')
    device_path[i]='/dev/'+device_path[i].replace('../../','')
    #specific name cleaning
    ##Dylos
    template='Prolific_Technology_Inc._USB-Serial_Controller_D'
    if(device_name[i].rfind(template)==0):
      device_name[i]='dylos0'
    ##ArduinoUNO
   #usb-Arduino__www.arduino.cc__0043_5533330393435190F171-if00
    template='Arduino__www.arduino.cc__0043_' #take last 8 characters as for others below
    if(device_name[i].rfind(template)==0):
    # device_name[i]='UNO0'
      device_name[i]=device_name[i].replace('Arduino__www.arduino.cc__0043_','')
##      device_name[i]=device_name[i].tail(8) #last 8 characters
    ##FTDI_FT232R: WaspMote, AlphaSenseCO2, MX3cK/ADC
    template='FTDI_FT232R_USB_UART_'
    if(device_name[i].rfind(template)==0):
      device_name[i]=device_name[i].replace(template,'')
  #  print device_name[i], device_path[i]

  return device_path,device_name

def get_serial_device_name(path):
  device_path,device_name=get_serial_pathNdevice_names()
  i=0
  while(path.rfind(device_path[i])!=0):
    i+=1
  return device_name[i]

#script call
import argparse
if __name__ == "__main__":
  #CLI arguments
  serialDev='' #e.g. '/dev/ttyUSB0'
  parser = argparse.ArgumentParser(
    description='show Xsensor device name either all device list or a specific device from /dev/tty????'
      +'   e.g. ./xsensor_device.py'
      +'or e.g. ./xsensor_device.py --device /dev/ttyUSB0'
    )
  parser.add_argument('-d','--device',default=serialDev, help='USB device name (e.g. /dev/ttyUSB0)')
  parser.add_argument('-v','--version',action='version',version='%(prog)s '+version)
  args = parser.parse_args()

  #--device CLI argument
  serialDev=args.device

  #print out device(s)
  if(len(serialDev)==0):
  ##device list
    device_path,device_name=get_serial_pathNdevice_names()
    for i in range(0,len(device_name)):
      print device_name[i], device_path[i]
  else:
  ##specified device
    print get_serial_device_name(serialDev)
